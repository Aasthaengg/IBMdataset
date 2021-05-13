s = input()
l = []
n = len(s)
dp = [[0] * 13 for i in range(n)]
mod = 1000000007
for i in range(n):
    l.append(pow(10, i, 13))
if s[-1] == "?":
    for i in range(10):
        dp[0][i] += 1
else:
    dp[0][int(s[-1])] += 1
for i in range(n-1):
    if s[n-2-i] == "?":
        for j in range(10):
            for k in range(13):
                dp[i+1][(j*l[i+1]+k)%13] += dp[i][k]
                dp[i+1][(j*l[i+1]+k)%13] %= mod
    else:
        for k in range(13):
            dp[i+1][(int(s[n-2-i])*l[i+1]+k)%13] += dp[i][k]
            dp[i+1][(int(s[n-2-i])*l[i+1]+k)%13] %= mod
print(dp[-1][5])