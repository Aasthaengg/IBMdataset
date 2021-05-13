import sys
input = sys.stdin.buffer.readline

mod = 998244353
n,s = map(int,input().split())
a = list(map(int,input().split()))


dp = [[0]*(s+1) for i in range(n)]

for i in range(n):
    if i == 0:
        dp[0][0] = 2
        if a[i] < s+1:
            dp[0][a[i]] = 1
        continue

    for j in range(s+1):
        dp[i][j] = dp[i-1][j]*2 %mod
        if j >= a[i]:
            dp[i][j] = (dp[i][j] + dp[i-1][j-a[i]])%mod

print(dp[-1][-1]%mod)
    
