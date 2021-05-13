n,m=map(int,input().split())
c=list(map(int,input().split()))

c.sort()

dp=[[500000]*(n+1) for i in range(m)]

for ni in range(0,n+1):
    dp[0][ni]=ni

for mi in range(0,m-1):
    for ni in range(n+1):
        if c[mi+1]>ni:
            dp[mi+1][ni]=dp[mi][ni]
        else:
            dp[mi+1][ni]=min(dp[mi+1][ni-c[mi+1]]+1,dp[mi][ni])
#    print(dp[mi])

print(dp[m-1][n])            
