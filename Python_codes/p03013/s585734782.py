mod = 10 ** 9 + 7

n, m = map(int, input().split())
A = [int(input()) for _ in range(m)]
not_wet = [True] * (n + 1)
for a in A:
    not_wet[a] = False
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    if not_wet[i]:
        if i == 1:
            dp[i] = dp[i - 1] % mod
        else:
            dp[i] = dp[i - 1] + dp[i - 2] % mod
print(dp[n] % mod)
