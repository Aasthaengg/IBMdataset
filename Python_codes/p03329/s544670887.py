N = int(input())

dp = [10 ** 9] * 100001
dp[0] = 1

for i in range(N):
    if dp[i] > 0:
        dp[i + 1] = min(dp[i] + 1, dp[i + 1])
        for j in range(1, 7):
            if 6 ** j + i <= N:
                dp[i + 6 ** j] = min(dp[i] + 1, dp[i + 6 ** j])
            if 9 ** j + i <= N:
                dp[i + 9 ** j] = min(dp[i] + 1, dp[i + 9 ** j])

print(dp[N] - 1)
