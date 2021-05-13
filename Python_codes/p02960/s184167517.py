S = input()
mod = 13
mp = 10**9+7
n = len(S)
dp = [[0]*13 for i in range(n+1)]
dp[-1][0] = 1
d = 1
for i in range(n):
    s = S[-i-1]
    if s=="?":
        for k in range(10):
            for j in range(13):
                l = (k*d + j)%mod
                dp[i][l] +=dp[i-1][j]
                dp[i][l] %=mp
    else:
        for j in range(13):
            l = (int(s)*d + j)%mod  
            dp[i][l] = dp[i-1][j]
    d = d*10 %mod
print(dp[n-1][5])
