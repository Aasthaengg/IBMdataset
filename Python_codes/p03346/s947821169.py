# 解説AC
N = int(input())
MAXN = 2 * 10 ** 5

dp = [0] * (MAXN + 1)

for _ in range(N):
    p = int(input())
    dp[p] = dp[p - 1] + 1

print(N - max(dp))