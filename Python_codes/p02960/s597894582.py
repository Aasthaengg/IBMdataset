s = input()
s = s[::-1]
n = len(s)
mod = 10**9 + 7

dp = [[0 for j in range(13)] for i in range(n)]
if s[0] == '?':
    for i in range(10):
        dp[0][i] = 1
else:
    num = int(s[0])
    dp[0][num] = 1

mul = 1
for i in range(1, n):
    mul = (mul*10) % 13
    if s[i] == '?':
        for m in range(10):
            num = (m * mul) % 13
            for j in range(13):
                dp[i][(j+num)%13] = (dp[i][(j+num)%13] + dp[i-1][j]) % mod
    else:
        num = (int(s[i]) * mul) % 13
        for j in range(13):
            dp[i][(j+num)%13] = (dp[i][(j+num)%13] + dp[i-1][j]) % mod

print(dp[n-1][5])