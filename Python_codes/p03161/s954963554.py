N, K = [int(i) for i in input().split(' ')]
h = [int(hi) for hi in input().split(' ')]

dp = [float('inf')] * N
dp[0] = 0

for i in range(N - 1):
    for k in range(i + 1, min(i + K + 1, N)):
        dp[k] = min(dp[k], dp[i] + abs(h[i] - h[k]))

print(dp[-1])
