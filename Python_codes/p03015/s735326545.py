L = input()
N = len(L)
mod = 10 ** 9 + 7
dp = [[0] * 2 for _ in range(100005)]
dp[0][0] = 1
for i in range(N):
    # a + b = 0
    if L[i] == "0":
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][1] = (dp[i][0] + dp[i][1]) % mod

    # a + b = 1
    if L[i] == "0":
        dp[i + 1][1] += dp[i][1] * 2 % mod
        dp[i + 1][1] %= mod
    else:
        dp[i + 1][0] += dp[i][0] * 2 % mod
        dp[i + 1][0] %= mod
        dp[i + 1][1] += dp[i][1] * 2 % mod
        dp[i + 1][1] %= mod

ans = dp[N][0] + dp[N][1]
print(ans % mod)