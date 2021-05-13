N = int(input())

dp = [-1]*(N+1)
dp[0] = 0
dp[1] = 1
for i in range(1, N+1):
    if dp[i] == -1:
        dp[i] = dp[i-1] + 1
        k = 6
        while i >= k:
            dp[i] = min(dp[i], dp[i-k]+1)
            k *= 6
        l = 9
        while i >= l:
            dp[i] = min(dp[i], dp[i-l]+1)
            l  *= 9
print(dp[N])