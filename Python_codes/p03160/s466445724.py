N = int(input())
h = list(map(int, input().split(" ")))

dp = [float("inf")]*(N)
dp[0] = 0

for i in range(N-1):
    dp[i + 1] = min(dp[i + 1], abs(h[i + 1] - h[i]) + dp[i])
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], abs(h[i + 2] - h[i]) + dp[i])

print(dp[-1])