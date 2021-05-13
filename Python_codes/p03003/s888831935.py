import sys
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,m = na()
s = na()
t = na()
mod = 10**9+7

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if (s[i-1] == t[j-1]):
            dp[i][j] = (1 + dp[i][j-1] + dp[i-1][j])%mod
        else:
            dp[i][j] = (dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1])%mod
  
print((dp[n][m]+1)%mod)