INF = 10**18

N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [INF for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    for k in range(1, K + 1):
        if i - k < 0:
            break
        dp[i] = min(dp[i], dp[i - k] + abs(H[i] - H[i - k]))

print(dp[N - 1])