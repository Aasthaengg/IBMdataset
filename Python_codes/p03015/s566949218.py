mod = 1000000007

l = input()
n = len(l)
dp = [[0, 0] for _ in range(n+1)]

dp[0][1] = 1
for i in range(n):
    if l[i] == '1':
        dp[i + 1][0] = (dp[i][0] * 3 + dp[i][1]) % mod
        dp[i + 1][1] = (dp[i][1] * 2) % mod
    else:
        dp[i + 1][0] = (dp[i][0] * 3) % mod
        dp[i + 1][1] = dp[i][1]
print((dp[n][0] + dp[n][1]) % mod)
