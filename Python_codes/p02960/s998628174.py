s = input()[::-1]

mod = 10 ** 9 + 7
dp = [[0] * 13 for _ in range(len(s)+1)]

dp[0][0] = 1
keta = 1
for i in range(len(s)):
    for j in range(13):
        if s[i] == '?':
            for k in range(10):
                dp[i+1][(k*keta+j)%13] += dp[i][j] 
                dp[i+1][(k*keta+j)%13] %= mod 
        else:
            dp[i+1][((int(s[i]))*keta+j)%13] += dp[i][j] 
            dp[i+1][((int(s[i]))*keta+j)%13] %= mod
    keta = (keta * 10) % 13

print(dp[-1][5]%mod)