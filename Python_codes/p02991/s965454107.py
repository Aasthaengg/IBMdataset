# https://atcoder.jp/contests/abc132/tasks/abc132_e
# 拡張ダイクストラ

import heapq
from collections import defaultdict

INF = int(1e18)
N, M = map(int, input().split())
G = {n: [] for n in range(N)}
for _ in range(M):
    ui, vi = map(int, input().split())
    ui -= 1; vi -= 1
    G[ui].append((1, vi))
S, T = map(int, input().split()); S -= 1; T -= 1

Gp = {}
for n in G:
    for t in [0, 1, 2]:
        Gp[(n, t)] = []
for u in G:
    for c, v in G[u]:
        Gp[(u, 0)].append((c, (v, 1))) # Gp[(v, 1)].append((1, (u, 0)))
        Gp[(u, 1)].append((c, (v, 2))) # Gp[(v, 2)].append((1, (u, 1)))
        Gp[(u, 2)].append((c, (v, 0))) # Gp[(v, 0)].append((1, (u, 2)))

# dijkstra on Gp
s = (S, 0)
t = (T, 0)
d = {v: INF for v in Gp}
used = {v: True for v in Gp}
d[s] = 0
used[s] = False

edgelist = []
for e in Gp[s]:
    heapq.heappush(edgelist, e)

while len(edgelist) > 0:
    minedge = heapq.heappop(edgelist)
    if not used[minedge[1]]:
        continue
    v = minedge[1]
    d[v] = minedge[0]
    used[v] = False
    for e in Gp[v]:
        if used[e[1]]:
            heapq.heappush(edgelist, (e[0] + d[v], e[1]))

if t not in d or d[t] == INF:
    print("-1")
else:
    print(d[t] // 3)