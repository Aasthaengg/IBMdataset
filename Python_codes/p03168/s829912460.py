n=int(input())
h=list(map(float,input().split()))

dp=[[1.0]*(n+1) for i in range(n+1)]
dp[0][0]=1.0

for i in range(1,n+1):
    dp[0][i]=0.0

for i in range(1,n+1):
    dp[i][0]=dp[i-1][0]*(1.0-h[i-1])

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]= h[i-1]*dp[i-1][j-1]+ (1-h[i-1])*dp[i-1][j]

ans=0
for i in range(n//2+1,n+1):
    ans+=dp[n][i]
print(ans)
