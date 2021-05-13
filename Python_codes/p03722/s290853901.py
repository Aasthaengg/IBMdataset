# BFS
# 現在の頂点、スコア、通過した頂点の数、を状態量としてもち、2*n個まで試す
# n個より多いものが最大になるのなら'inf'を出力
from collections import deque
from sys import stdin
def input():
    return stdin.readline().strip()

inf = float('inf')

n, m = map(int, input().split())

edge = [[] for _ in range(n)]
weight = [[] for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    edge[i].append(j)
    weight[i].append(k)

seen = [-inf] * n
todo = deque([(0, 0, 1)])
while len(todo) > 0:
    node, score, num = todo.popleft()
    if num > 2 * n:
        break

    for i in range(len(edge[node])):
        if seen[edge[node][i]] < score + weight[node][i]:
            seen[edge[node][i]] = score + weight[node][i]
            todo.append((edge[node][i], score + weight[node][i], num + 1))
            if edge[node][i] == n - 1 and num >= n:
                print('inf')
                exit()

print(seen[n-1])