m,n=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
dp=[[int(1e4) for i in range(m+1)] for j in range(n+1)]
i=n-1
while i>=0:
    for j in range(m+1):
        if j==c[i]:
            dp[i][j]=1
        elif j<c[i]:
            dp[i][j]=dp[i+1][j]
        else:
            dp[i][j]=min(dp[i+1][j],dp[i+1][j-c[i]]+1,dp[i][j-c[i]]+1)
    i-=1
print(dp[0][m])