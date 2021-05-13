N = int(input())
dp = [float('inf')]*(N+1)
dp[0] = 0
for i in range(N+1):
    if i+1 <= N:
        dp[i+1] = min(dp[i+1],dp[i]+1)
    for j in range(1,N+1):
        if i + 6**j > N:
            break
        dp[i+6**j] = min(dp[i+6**j],dp[i]+1)
    for k in range(1,N+1):
        if i + 9**k > N:
            break
        dp[i+9**k] = min(dp[i+9**k],dp[i]+1)
print(dp[N])