# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/11/ALDS1_11_C

from collections import deque

n = int(input())
graph = {}
res = [-1 for i in range(n + 1)]

for i in range(1, n + 1):
    data = input().split()
    graph[i] = [int(i) for i in data[2:]]

visited = set()
q = deque()
q.append((1, 0))  # node,distance
visited.add(1)

while q:
    node, dis = q.popleft()
    res[node] = dis
    for _next in graph[node]:
        if _next not in visited:
            visited.add(_next)
            q.append((_next, dis + 1))

for i in range(1, n + 1):
    print(i, res[i])

