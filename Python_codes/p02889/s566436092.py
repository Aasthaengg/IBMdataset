import sys
sys.setrecursionlimit(10 ** 9)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

INF = 10 ** 15

def warshall_floyd(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

N, M, L = lr()
dist = [[INF] * (N+1) for _ in range(N+1)] # 1-indexed
for _ in range(M):
    a, b, c = lr()
    if c > L:
        continue
    dist[a][b] = c
    dist[b][a] = c

dist = warshall_floyd(dist, N+1)
supply = [[INF] * (N+1) for _ in range(N+1)] # 1-indexed 距離L以下で供給が1回必要
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if dist[i][j] <= L:
            supply[i][j] = supply[j][i] =  1

supply = warshall_floyd(supply, N+1)
Q = ir()
for _ in range(Q):
    s, t = lr()
    x = supply[s][t] - 1
    print(-1 if x + 1 == INF else x)
