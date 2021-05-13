
from collections import deque

N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N * N)]
inserted = [0] * (N * N)
for i, nodes in enumerate(X):
    for j1, j2 in zip(nodes[:-1], nodes[1:]):
        n1 = max(i, j1 - 1) * N + min(i, j1 - 1)
        n2 = max(i, j2 - 1) * N + min(i, j2 - 1)
        graph[n1].append(n2)
        inserted[n2] += 1

dist = [0] * (N * N)
visited = [False] * (N * N)
for i in range(N):
    visited[i * N + i] = True

q = deque()
for i, v in enumerate(inserted):
    if v == 0:
        q.append(i)
        visited[i] = True
        dist[i] = 1

while q:
    u = q.popleft()
    for v in graph[u]:
        if visited[v]:
            continue

        inserted[v] -= 1
        if inserted[v] == 0:
            visited[v] = True
            dist[v] = dist[u] + 1
            q.append(v)

print(max(dist) if all(visited) else -1)
