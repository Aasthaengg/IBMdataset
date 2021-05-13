s=input()
lim=10**9+7
dp = [[0 for _ in range(13)] for _ in range(len(s))]
if s[0] =="?":
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(s[0])] = 1

for i in range(1,len(s)):
    for j in range(13):
        if s[i] ==  "?":
            for k in range(10):
                dp[i][(j*10 + k)%13] = (dp[i][(j*10 + k)%13]+dp[i-1][j])%lim
        else:
            dp[i][(j*10 + int(s[i]))%13] = (dp[i][(j*10 + int(s[i]))%13]+dp[i-1][j])%lim
print(dp[-1][5])