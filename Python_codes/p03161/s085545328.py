N, K = map(int, input().split())
*h, = map(int, input().split())
dp = [float("inf")] * N
dp[0] = 0
for i in range(1, N):
    for j in range(max(0, i-K), i):
        a = dp[j] + abs(h[i] - h[j])
        dp[i] = min(dp[i], a)
print(dp[-1])