import sys

N, K = map(int, input().split())
steps = list(map(int, input().split()))

dp = [sys.maxsize] * N
dp[0] = 0
for i in range(1, N):
    limit = K if K <= i else i
    for j in range(1, limit + 1):
        a = abs(steps[i] - steps[i - j]) + dp[i - j]
        dp[i] = a if a < dp[i] else dp[i]

print(dp[N - 1])
