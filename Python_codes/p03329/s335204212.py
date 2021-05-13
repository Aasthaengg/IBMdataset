n=int(input())
dp=[10**3]*(n+1)
dp[0]=0

for i in range(1,n+1):
    j=6
    for _ in range(10):
        if j<=i:
            dp[i]=min(dp[i],dp[i-j]+1)
        j*=6
    
    j=9
    for _ in range(10):
        if j<=i:
            dp[i]=min(dp[i],dp[i-j]+1)
        j*=9
    dp[i]=min(dp[i],dp[i-1]+1)
print(dp[-1])