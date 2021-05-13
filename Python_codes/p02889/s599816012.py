INF = 10**10

def warshall_floyd(d):
    # d[i][j]: ij間の最小コスト
    # i=jのとき0, i!=jのときINFで初期化
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

N, M, L = map(int, input().split())
dist = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    dist[a][b] = c; dist[b][a] = c
dist = warshall_floyd(dist)

dist2 = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            dist2[i][i] = 0
        else:
            if dist[i][j] <= L:
                dist2[i][j] = 1
dist2 = warshall_floyd(dist2)

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1; t -= 1
    if dist2[s][t] == INF:
        print(-1)
    else:
        print(dist2[s][t]-1)