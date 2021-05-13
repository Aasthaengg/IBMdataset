s = str(input())
dp = [[0] * 13 for i in range(len(s)+1)]
dp[0][0] = 1
Naoppy = 1
mod = 13
ansmod = 10 ** 9 + 7
ans = 0
for i in range(len(s)):
    if s[i] == "?":
        for j in range(10):
            for k in range(13):
                dp[i+1][(k * 10 +j)%mod] += dp[i][k]
    else:
        for k in range(13):
            dp[i+1][(k * 10 + (int(s[i])))%mod] += dp[i][k]
    for j in range(13):
        dp[i+1][j] %= ansmod
  #    print(dp)
print(dp[len(s)][5])