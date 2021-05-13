N,M=list(map(int,input().split()))
xyz=[list(map(int,input().split())) for _ in range(N)]

dp=[[[-10**15]*8 for _ in range(N+1)] for _ in range(N+1)]
sign={0:1,1:-1}
ans=0

for i in range(2**3):
    signlst=[1]*3

    for j in range(N):
        dp[j][0][i]=0

    for j in range(3):
        signlst[j]=sign[(i>>j)&1]
    
    for j in range(N):
        for k in range(N):
            dp[j+1][k+1][i]=max(dp[j][k+1][i],dp[j][k][i]+sum([signlst[l]*xyz[j][l] for l in range(3)]))
    
    ans=max(ans,dp[N][M][i])

print(ans)