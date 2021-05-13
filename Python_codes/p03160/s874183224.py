import sys

N = int(sys.stdin.readline())
h = [int(hi) for hi in sys.stdin.readline().split(' ')]

dp = [1000000 * N] * N
dp[0] = 0

for i in range(N - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
    if i < N - 2:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))

print(dp[-1])
