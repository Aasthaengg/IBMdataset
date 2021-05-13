s = input().rstrip()

n = [0] * 13
for i in range(13):
    n[i] = (i * 10) % 13

rev = [0] * 13
for i, ni in enumerate(n):
    rev[ni] = i

dp = [[0] * 13 for _ in range(len(s))]

if s[0] == '?':
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(s[0])] = 1

mod = 10**9 + 7
for i in range(1, len(s)):
    for j in range(13):
        if s[i] == '?':
            for k in range(10):
                dp[i][j] += dp[i-1][rev[(j-k) % 13]]
                dp[i][j] %= mod
        else:
            dp[i][j] = dp[i-1][rev[(j-int(s[i])) % 13]]

print(dp[-1][5])