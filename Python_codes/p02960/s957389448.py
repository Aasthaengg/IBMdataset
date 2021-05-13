s = input()
n = len(s)
mod = 10**9 + 7
dp = [[0 for i in range(13)] for i in range(n)]
if s[n-1] == "?":
    for i in range(10):
        dp[n-1][i] = 1
else:
    dp[n-1][int(s[n-1])] = 1
now = 1
for i in reversed(range(n-1)):
    now *= 10
    now %= 13
    if s[i] == "?":
        for j in range(10):
            amari = (j * now) % 13
            for k in range(13):
                dp[i][(k+amari)%13] += dp[i+1][k]
                dp[i][(k+amari)%13] %= mod
    else:
        amari =(int(s[i]) * now) % 13
        for k in range(13):
            dp[i][(k+amari)%13] += dp[i+1][k]
            dp[i][(k+amari)%13] %= mod
print(dp[0][5])