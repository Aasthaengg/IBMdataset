N, M, L = map(int, input().split())
INF = 10 ** 12

G = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a][b] = c
    G[b][a] = c


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

GL = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N):
    for j in range(i+1, N+1):
        if G[i][j] <= L:
            GL[i][j] = 1
            GL[j][i] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            GL[i][j] = min(GL[i][j], GL[i][k] + GL[k][j])

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    ans = GL[s][t]
    if ans == INF:
        print(-1)
    else:
        print(ans-1)


