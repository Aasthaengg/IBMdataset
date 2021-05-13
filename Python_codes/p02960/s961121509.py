s = input()
n = len(s)
mod = 1000000007
dp = [[0 for i in range(13)] for j in range(n+1)]
dp[0][0] = 1
s = s[::-1]
dec = 1
for i in range(n):
    x = s[i]
    dec %= 13
    if x != '?':
        x = int(x)
        r = (dec * x) % 13
        for j in range(13):
            dp[i+1][j] = dp[i][(j-r)%13]
    else:
        for j in range(10):
            r = (dec * j) % 13
            for k in range(13):
                dp[i+1][k] += dp[i][(k-r)%13] % mod
    dec *= 10
print(dp[-1][5] % mod)
#print(dp)        