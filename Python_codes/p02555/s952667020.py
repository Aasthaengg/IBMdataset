mod=10**9+7
s=int(input())
dp=[0]*2005
dp[0]=1
for i in range(2005):
    for j in range(i+3,2005):
        dp[j]=dp[i]+dp[j-1]
print(dp[s]%mod)
