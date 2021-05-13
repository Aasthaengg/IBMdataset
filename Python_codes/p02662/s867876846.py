import sys
import math
def input():
    return sys.stdin.readline()[:-1]
mod = 998244353
n,s=map(int,input().split())
a = list(map(int,input().split()))
dp =[[0 for i in range(s+1)]for j in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    for j in range(s+1):
        if j-a[i-1]>=0:
            dp[i][j] += dp[i-1][j-a[i-1]]
            dp[i][j] %= mod

        dp[i][j] += dp[i-1][j]*2
        dp[i][j] %= mod

print(dp[n][s])
