n,m = map(int,input().split())
mp = [False]*(n+1)
for i in range(m):
    a=int(input())
    mp[a]=True
mod = 10**9 + 7

dp = [[0]*2 for i in range(n+1)]
dp[0][0] = 1

for i in range(0,n):
    if(mp[i]):
        continue
    for j in range(2):
        if(dp[i][j]==0):
            continue
        if(not mp[i+1]):
            dp[i+1][0] += dp[i][j]
            dp[i+1][0] %= mod
        if(i==(n-1)):
            continue
        if(not mp[i+2]):
            dp[i+2][1] += dp[i][j]
            dp[i+2][1] %= mod

ans = (dp[-1][0]+dp[-1][1])%mod

print(ans)