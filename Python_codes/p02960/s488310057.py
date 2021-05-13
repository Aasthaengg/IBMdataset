s = input()

mod = 10**9 + 7
l = len(s)
dp = [[0] * 13 for _ in range(l+1)]
dp[0][0] = 1
for i in range(1, l+1):
    if s[i-1] == '?':
        for j in range(10):
            for k in range(13): 
                dp[i][(k * 10 + j) % 13] = (dp[i][(k * 10 + j) % 13] + dp[i-1][k]) % mod
    else:
        for k in range(13):
            dp[i][(k * 10 + int(s[i-1])) % 13] = (dp[i][(k * 10 + int(s[i-1])) % 13] + dp[i-1][k]) % mod
print(dp[l][5])