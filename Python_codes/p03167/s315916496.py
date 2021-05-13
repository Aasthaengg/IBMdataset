#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

M = 10**9+7
h,w = ip()
grid = [input().strip() for i in range(h)]
dp = [[0]*w for i in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if i-1 >= 0 and grid[i-1][j] == '.':
            dp[i][j] += dp[i-1][j]
        if j-1 >= 0 and grid[i][j-1] == '.':
            dp[i][j] += dp[i][j-1]
        dp[i][j] %= M
print(dp[-1][-1]%M)
