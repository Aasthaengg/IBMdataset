import sys
from heapq import heappop, heappush

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
# 3*N頂点あるとする
edges = [[] for _ in range(3*N + 4)] # 3-indexed
for _ in range(M):
    u, v = lr()
    u *= 3; v *= 3
    edges[u].append(v+1)
    edges[u+1].append(v+2)
    edges[u+2].append(v)

INF = 10 ** 18

def dijkstra(start):
    dist = [INF] * (3*N+4)
    dist[start] = 0
    que = [(0, start)]
    while que:
        d, v = heappop(que)
        if dist[v] < d:
            continue
        for next in edges[v]:
            d1 = d + 1
            if dist[next] > d1:
                dist[next] = d1
                heappush(que, (d1, next))
    return dist

S, T = lr()
dist = dijkstra(S*3)
if dist[T*3] == INF:
    print(-1)
else:
    print(dist[T*3] // 3)
