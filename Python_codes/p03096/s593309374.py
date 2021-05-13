n = int(input())
c = [int(input()) for _i in range(n)]
c.append(-1)
dic = [-1 for _i in range(10**5 *2 +1)]
dp = [0 for _i in range(n+1)]
dp[n] = 1
mod = 10**9 +7
for i in range(n):
    if c[i-1] != c[i]:
        if dic[c[i]] > 0:
            dp[i] = (dp[i-1] + dic[c[i]])%mod
        else:
            dp[i] = dp[i-1]
        dic[c[i]] = dp[i]
    else:
        dp[i] = dp[i-1]
    
print(dp[n-1]%mod)