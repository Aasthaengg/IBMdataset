
N, M = map(int, input().split())
X = [int(input()) for _ in range(M)]

MOD = 10 ** 9 + 7
dp = [-1] * (N + 1)
dp[0] = 1
for i in range(M):
    dp[X[i]] = 0

for i in range(N):
    if dp[i + 1] < 0:
        if i == 0:
            dp[i + 1] = dp[i]
        else:
            dp[i + 1] = (dp[i] + dp[i - 1]) % MOD

print(dp[-1])
