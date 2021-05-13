from copy import deepcopy
import sys
input = sys.stdin.readline


def floyd_warshall(dist):
    v = len(dist)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dist = deepcopy(A)
floyd_warshall(dist)
edges = []
for u in range(N-1):
    for v in range(u+1, N):
        edges.append((A[u][v], u, v))
edges.sort()
ans = 0
for d, u, v in edges:
    if dist[u][v] < d:
        ans = -1
        break
    ok = False
    for w in range(N):
        if w == u or w == v:
            continue
        if dist[u][w] + dist[w][v] == dist[u][v]:
            ok = True
            break
    if not ok:
        ans += d
print(ans)
