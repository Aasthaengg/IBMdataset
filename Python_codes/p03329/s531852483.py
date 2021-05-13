n = int(input())
dp = [n+1 for i in range(n+1)]
dp[0] = 0
for i in range(n):
    dp[i+1] = min(dp[i]+1, dp[i+1])
    j = 1
    while i + 6 ** j <= n:
        dp[i+6**j] = min(dp[i]+1, dp[i+6**j])
        j += 1
    j = 1
    while i + 9 ** j <= n:
        dp[i+9**j] = min(dp[i]+1, dp[i+9**j])
        j += 1
print(dp[n])