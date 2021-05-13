n,ma,mb=map(int,input().split())
abc=[list(map(int,input().split())) for _ in range(n)]

wmax=400
inf=10**10
dp=[[[inf]*(wmax+1) for _ in range(wmax+1)] for _ in range(n+1)]
dp[0][0][0]=0

for i in range(n):
    a,b,c=abc[i]
    for j in range(wmax+1):
        for k in range(wmax+1):
            dp[i+1][j][k]=dp[i][j][k]

            if j>=a and k>=b:
                dp[i+1][j][k]=min(dp[i+1][j][k],dp[i][j-a][k-b]+c)

ans=inf

for j in range(1,wmax+1):
    for k in range(1,wmax+1):
        if dp[n][j][k]>=inf:
            continue

        if ma*k==mb*j:
            ans=min(ans,dp[n][j][k])

if ans==inf:
    print(-1)
else:
    print(ans)
