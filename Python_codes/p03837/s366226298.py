import heapq
from collections import defaultdict

def dijkstra(i, V, E, INF=1e9):
    D = [INF for v in V]
    D[i] = 0
    Q = [(d, v) for v, d in enumerate(D)]
    heapq.heapify(Q)
    prev = [None for v in V]

    while len(Q) > 0:
        du, u = heapq.heappop(Q)
        for v, (duv, *_) in E[u].items():
            dv = du + duv
            if D[v] > dv:
                D[v] = dv
                prev[v] = u
                heapq.heappush(Q, (dv, v))
    return prev

def count_path(prev, E):
    x = [(i, p) for i, p in enumerate(prev)]
    while len(x) > 0:
        i, p = x.pop()
        if p is not None:
            E[i][p][-1] += 1
            E[p][i][-1] += 1
            x.append((p, prev[p]))
    return E

n, m = map(int, input().split())
E_list = [list(map(int, input().split())) for _ in range(m)]
E = defaultdict(dict)
for j in range(m):
    a, b, c = E_list[j]
    E[a][b] = [c, 0]
    E[b][a] = [c, 0]
V = list(range(n + 1))

for i in range(1, n + 1):
    prev = dijkstra(i, V, E)
    E = count_path(prev, E)

ans = 0
for v1 in E.values():
    for v2 in v1.values():
        ans += (v2[-1] == 0)
print(ans // 2)
