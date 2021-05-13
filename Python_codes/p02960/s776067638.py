s = input()
len_s = len(s)
mod = 10 ** 9 + 7
dp = [[0] * 13 for i in range(len_s)]
if s[-1] == '?':
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(s[-1])] = 1

digits = 1
for i in range(1, len_s):
    digits = (digits * 10)%13
    for j in range(13):

        if dp[i - 1][j] > 0:
            if s[-(i + 1)] != '?':
                add = int(s[-(i + 1)]) * digits
                dp[i][(j + add)%13] = (dp[i][(j + add)%13] + dp[i - 1][j])%mod
            else:
                for k in range(10):
                    # k:先頭に加える数字
                    add = k * digits
                    dp[i][(j + add) % 13] = (dp[i][(j + add) % 13] + dp[i - 1][j]) % mod

print(dp[-1][5] % mod)