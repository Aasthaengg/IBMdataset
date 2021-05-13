s = input()
S = len(s)

mod = 10**9+7

#全ての余りを確認する
dp = [[0 for i in range(13)]for j in range(S)]

if s[0] == "?":
    for i in range(10):
        dp[0][i%13] += 1
else:
    dp[0][int(s[0])%13] += 1

for i in range(1,S):
    if s[i] == "?":
        for j in range(10):
            for k in range(13):
                dp[i][(10*k+j)%13] += dp[i-1][k]%mod
    else:
        for k in range(13):
            dp[i][(10*k+int(s[i]))%13] += dp[i-1][k]%mod
            
print(dp[-1][5]%mod)