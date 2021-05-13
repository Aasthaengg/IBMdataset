s = input()
n = len(s)
mod = 10 ** 9 + 7
amari = [1]
for i in range(n - 1):
    amari.append(amari[-1] * 10 % 13)
amari.reverse()
dp = [[0 for i in range(13)] for j in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(13):
        if s[i] == "?":
            temp = 0
            for k in range(10):
                temp += dp[i][(j - amari[i] * k) % 13]
                temp %= mod
            dp[i + 1][j] = temp
        else:
            num = int(s[i])
            dp[i + 1][j] = dp[i][(j - amari[i] * num) % 13]
print(dp[n][5])