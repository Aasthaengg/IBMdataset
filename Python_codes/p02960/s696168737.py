s = input()

n = len(s)
mod = 10**9+7

dp = [[0]*13 for i in range(n+1)]
dp[0][0]=1

for i in range(n):
    if s[-1-i]=='?':
        p = [x*pow(10,i,13) for x in range(0,10)]
    else:
        p = [int(s[-1-i])*pow(10,i,13)]
    for j in range(13):
        for x in p:
            dp[i+1][(j+x)%13] += dp[i][j]
    for j in range(13):
        dp[i+1][j]%=mod

print(dp[-1][5])
