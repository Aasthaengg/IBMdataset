
N,M,L = map(int,input().split())
ABC = [list(map(int,input().split())) for _ in range(M)]
Q = int(input())
st = [list(map(int,input().split())) for _ in range(Q)]

INF = 1<<30
dp = [[INF]*N for _ in range(N)]

for a,b,c in ABC:
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
        
d = [[INF]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if dp[i][j]<=L:
            d[i][j] = 1
        
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])
        
for s,t in st:
    if d[s-1][t-1]!=INF:
        print(d[s-1][t-1]-1)
    else:
        print(-1)