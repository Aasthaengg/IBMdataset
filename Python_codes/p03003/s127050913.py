import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = tuple(map(int,input().split()))
t = tuple(map(int,input().split()))

mod = 10**9+7

dp = [[0]*m for _ in [0]*n]
a = [[0]*m for _ in [0]*n]

for i in range(n):
    a[i][0] = a[i-1][0]
    if t[0] == s[i]:
        dp[i][0] = 1
        a[i][0] += 1

for i in range(m):
    a[0][i] = a[0][i-1]
    if s[0] == t[i]:
        dp[0][i] = 1
        a[0][i] += 1

for i in range(1,n):
    for j in range(1,m):
        if s[i] == t[j]:
            dp[i][j] = (a[i-1][j-1]+1)%mod
        a[i][j] = (a[i-1][j] + a[i][j-1] - a[i-1][j-1] + dp[i][j]) %mod

res = 1
for i in range(n):
    res = (res + sum(dp[i]))%mod
print(res%mod)