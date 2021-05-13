s=list(input())
s.reverse()
MOD=10**9+7
dp = [[0 for _ in range(13)] for _ in range(len(s)+1)]
dp[0][0]=1
for i in range(len(s)):
    nd=s[i]
    p=pow(10,i,13)
    for mod in range(13):
        dp[i][mod] %=MOD
        for d in range(10):
            if nd != "?" and str(d)!=nd:
                continue
            nmod=(d*p + mod) % 13
            dp[i+1][nmod] += dp[i][mod]

print(dp[-1][5]%MOD)