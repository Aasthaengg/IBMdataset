N = int(input())
dp = [float('inf')]*(N+1)
dp[0] = 0
for i in range(N+1):
    if i >= 1:
        dp[i] = min(dp[i-1]+1,dp[i])
    for j in range(1,N+1):
        if i < 6**j:
            break
        dp[i] = min(dp[i-6**j]+1,dp[i])
    for k in range(1,N+1):
        if i < 9**k:
            break
        dp[i] = min(dp[i-9**k]+1,dp[i])
print(dp[N])