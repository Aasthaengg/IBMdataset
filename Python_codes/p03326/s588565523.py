# ABC100D

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))


import itertools
n, m = map(int, input().split())
xs = [None] * n
ys = [None] * n
zs = [None] * n
for i in range(n):
    xs[i],ys[i],zs[i] = map(int, input().split())
best = 0
for sx, sy, sz in itertools.product(*[[-1, 1] for _ in range(3)]):
    dp = [[None]*(m+1) for _ in range(n+1)]
    for j in range(m+1):
        dp[0][j] = 0
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i>j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + sx*xs[i-1] + sy*ys[i-1] + sz*zs[i-1])
            else:
                dp[i][j] = dp[i-1][j-1] + sx*xs[i-1] + sy*ys[i-1] + sz*zs[i-1]
    best = max(best, dp[n][m])
#     print(dp[n][m])
print(best)