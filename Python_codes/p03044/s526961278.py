N = int(input())
g = [[] for i in range(N)]

for i in range(N-1):
    u, v, w = list(map(int, input().split()))
    u -= 1; v -= 1

    g[u].append((w, v))
    g[v].append((w, u))

from heapq import heappush, heappop, heapify
INF = float('inf')

dist = [INF] * N
visited = [False] * N

q = g[0]
heapify(q)
dist[0] = 0
visited[0] = True

while q:
    c, v = heappop(q)

    if visited[v]: continue
    visited[v] = True
    dist[v] = c

    for w, u in g[v]:
        if visited[u]: continue
        heappush(q, (c+w, u))

for i in range(N):
    if dist[i] % 2: print(0)
    else: print(1)