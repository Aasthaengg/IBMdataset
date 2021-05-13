import math


N, K = map(int, input().split())
h = [int(i) for i in input().split()]
dp = [10**9] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    for j in range(1, K + 1):
        if i - j < 0:
            break

        dp[i] = min(
            dp[i],
            dp[i - j] + abs(h[i] - h[i - j])
        )

print(dp[-1])
