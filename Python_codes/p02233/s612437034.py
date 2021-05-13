N = int(input())
dp = {0:1,1:1}
for i in range(1,N):
    dp[i+1] = dp[i]+dp[i-1]
print(dp[N])
