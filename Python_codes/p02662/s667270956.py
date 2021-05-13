n, s = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
U = 3010
dp = [0] * (U + 1)
dp[0] = 1
for a in A:
    dp2 = [0] * (s + 1)
    for j in range(s + 1):
        dp2[j] = dp[j] * 2
        if j >= a:
            dp2[j] += dp[j - a]
        dp2[j] %= MOD
    dp = dp2

print(dp[s])