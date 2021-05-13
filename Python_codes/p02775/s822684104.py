s = input()
l = len(s)

INF = float('inf')
dp = [[INF]*2 for _ in range(l+1)]
dp[0][0]=0
dp[0][1]=1
for i in range(l):
    num = int(s[i])
    dp0 = dp[i][0]
    dp1 = dp[i][1]
    dp[i+1][0] = min(dp0+num, dp1+min(10-num,num+1))
    dp[i+1][1] = min(dp0+num+1,dp1+10-num-1)

print(dp[-1][0])

