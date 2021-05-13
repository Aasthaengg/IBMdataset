MOD = 10**9 + 7
N, M = map(int, input().split())
a = [int(input()) for _ in range(M)] + [N + 1]
dp = [0] * (N + 1)
dp[0] = 1
s = -1

for broken in a:
    for j in range(s + 1, broken):
        if j > s + 1:
            dp[j] += dp[j - 1] % MOD
        if j > 1:
            dp[j] += dp[j - 2] % MOD
        dp[j] %= MOD
    s = broken

print(dp[-1])