n,m=map(int,input().split())
c=list(map(int,input().split()))
dp=[[i for i in range(n+1)] for _ in range(m+1)]
for i in range(1,m+1):
    for w in range(1,n+1):
        if c[i-1]>w:
            dp[i][w]=dp[i-1][w]
        else:
            dp[i][w]=min(dp[i][w-c[i-1]]+1,dp[i-1][w])
print(dp[m][n])
