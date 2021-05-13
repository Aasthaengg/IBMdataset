n=int(input())
dp=[99]*5000000
dp[0]=0
for i in range(n):
    for j in range(8):
        dp[i+6**j]=min(dp[i+6**j],dp[i]+1)
        dp[i+9**j]=min(dp[i+9**j],dp[i]+1)
print(dp[n])