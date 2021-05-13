# ABC130E

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))


M = 10**9+7
n,m = map(int, input().split())
s = input().split()
t = input().split()
n = len(s)
m = len(t)
dp = [[0] * (m+2) for _ in range(n+2)] # i-1, j-1で終わる部分列の組の個数
ss = [[0] * (m+2) for _ in range(n+2)] # sum(dp[0][0]+...+ dp[i-1][j-1])

for i in range(n+2):
    dp[i][0] = 0
    ss[i][0] = 0
for j in range(m+2):
    dp[0][j] = 0
    ss[0][j] = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i-1]==t[j-1]:
            dp[i][j] += (ss[i][j] + 1)
            dp[i][j] %= M
        ss[i+1][j+1] = (-ss[i][j]+ss[i+1][j]+ss[i][j+1]+dp[i][j]) % M
print(ss[n+1][m+1]+1)