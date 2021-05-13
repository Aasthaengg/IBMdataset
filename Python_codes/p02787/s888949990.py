H,N=map(int,input().split())
L=[tuple(map(int,input().split())) for i in range(N)]
dp=[[-1]*(H+1) for i in range(N+1)]
for d in dp:
    d[0]=0
dp[0]=[10**9]*(H+1)
i=1
for a,b in L:
    for j in range(H+1):
        if j<a:
            dp[i][j]=min(dp[i-1][j],b)
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-a]+b)
    i+=1
print(dp[N][H-1])