n,m,r = map(int,input().split())
v = list(map(int,input().split()))
for i in range(r):
    v[i] -= 1
INF = float("inf")
g = [[INF]*n for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    g[a][b] = c
    g[b][a] = c
for i in range(n): g[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j],g[i][k]+g[k][j])


dp = [[INF]*r for i in range(2**r)]
for i in range(r):
    dp[2**i][i] = 0


for i in range(1,2**r):
    for j in range(r):
        if dp[i][j] == INF:
            continue
        for k in range(r):
            nxt = i | 2**k
            dp[nxt][k] = min(dp[nxt][k],dp[i][j]+g[v[j]][v[k]])

print(min(dp[-1]))
