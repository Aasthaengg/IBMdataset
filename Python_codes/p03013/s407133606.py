n, m = map(int, input().split())
arr = set([int(input()) for _ in range(m)])

MOD = 10**9 + 7

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    if not i in arr:
        if i == 1:
            dp[i] = dp[i - 1] % MOD
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[-1])