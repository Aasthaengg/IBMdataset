s = input()

mod = 10 ** 9 + 7

dp = [[0] * 13 for _ in range(len(s))]

if s[0] == '?':
    dp[0] = [1] * 10 + [0] * 3
else:
    dp[0][int(s[0])] = 1

for i in range(len(s)-1):
    if s[i+1] == '?':
        for j in range(13):
            for k in range(10):
                dp[i+1][(j*10+k)%13] = (dp[i+1][(j*10+k)%13] + dp[i][j]) % mod
    else:
        n = int(s[i+1])
        for j in range(13):
            dp[i+1][(j*10+n)%13] = (dp[i+1][(j*10+n)%13] + dp[i][j]) % mod

print(dp[len(s)-1][5])