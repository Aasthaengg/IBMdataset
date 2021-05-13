n, m = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

import heapq
from collections import defaultdict
g1 = defaultdict(set)
for u, v in uv:
    g1[u-1].add(v-1)

s -= 1
t -= 1

dist = [[float('inf')] * 3 for _ in range(n)]
dist[s][0] = 0

q = [(0, s, 0)] # (dist, pos, kenken)
heapq.heapify(q)

while q:
    du, u, c = heapq.heappop(q)
    if dist[u][c] < du:
        continue
    c2 = (c + 1) % 3
    for v in g1[u]:
        if du + 1 < dist[v][c2]:
            dist[v][c2] = du + 1
            heapq.heappush(q, (dist[v][c2], v, c2))

if dist[t][0] != float('inf'):
    print(dist[t][0] // 3)
else:
    print(-1)
