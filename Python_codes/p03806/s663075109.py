N,Ma,Mb = map(int, input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
INF = 5000
dp=[[[INF]*(10*N+1) for _ in range(10*N+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    a,b,c=arr[i]
    for j in range(10*N+1):
        for k in range(10*N+1):
            if dp[i][j][k] == INF:
                continue
            dp[i+1][j][k]=min(dp[i+1][j][k],dp[i][j][k])
            dp[i+1][j+a][k+b]=min(dp[i+1][j+a][k+b],dp[i][j][k]+c)

ans=INF
for i in range(1,10*N+1):
        if i*Ma>10*N or i*Mb>10*N:
            break
        ans = min(ans, dp[N][i*Ma][i*Mb])
if ans == INF:
    print(-1)
else:
    print(ans)