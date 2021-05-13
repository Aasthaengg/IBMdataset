s=int(input())
m=10**9+7
dp=[0]*(s+1)
dp[0]=1
dp[1:3]=[0]*2
for i in range(3,s+1):
    dp[i]=(dp[i-1]+dp[i-3])%m
print(dp[s])