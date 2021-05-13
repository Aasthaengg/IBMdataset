n=int(input())
k=int(input())

dp=[0]*(n+1)
dp[0]=1

for i in range(1,n+1):
    dp[i]=min(dp[i-1]*2,dp[i-1]+k)

print(dp[n])