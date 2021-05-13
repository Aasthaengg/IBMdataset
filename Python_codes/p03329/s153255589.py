N = int(input())
dp = [i for i in range(N+1+9**5)]
for i in range(N):
  dp[i+1] = min(dp[i+1], dp[i] + 1)
  for j in range(1, 7):
    dp[i+6**j] = min(dp[i+6**j], dp[i] + 1)
  for k in range(1, 6):
    dp[i+9**k] = min(dp[i+9**k], dp[i] + 1)
    
print(dp[N])