INF = 10 ** 60


def li():
    return [int(x) for x in input().split()]


N, K = li()
H = li() + [INF] * K

dp = [INF] * (N + K)

dp[0] = 0

for i in range(N):
    for k in range(1, K+1):
        dp[i + k] = min(dp[i + k], dp[i] + abs(H[i + k] - H[i]))

print(dp[N - 1])