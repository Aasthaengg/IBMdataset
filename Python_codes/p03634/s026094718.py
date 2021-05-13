from sys import stdin

def input():
    return stdin.readline().strip()

n = int(input())
edge = [[] for _ in range(n)]
weight = [[] for _ in range(n)]
for _ in range(n-1):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    edge[i].append(j)
    edge[j].append(i)
    weight[i].append(k)
    weight[j].append(k)

q, k = map(int, input().split())

k -= 1
# root = k
# DFS
distance = [-1] * n
distance[k] = 0
todo = [k]
while len(todo) > 0:
    i = todo.pop(-1)
    for j in range(len(edge[i])):
        if distance[edge[i][j]] == -1:
            distance[edge[i][j]] = distance[i] + weight[i][j]
            todo.append(edge[i][j])

ans = []
for _ in range(q):
    i, j = map(int, input().split())
    ans.append(distance[i-1] + distance[j-1])

for i in ans:
    print(i)
