import sys 
input = sys.stdin.readline
mod = 10**9 + 7
h, w = [int(x) for x in input().split()]
g = [list(input().rstrip()) for _ in range(h)]

dp = [[0]*w for _ in range(h)]

dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if g[i][j] == "#":
            continue
        xy = [(i - 1, j), (i, j - 1)]
        for k in xy:
            x, y = k
            if 0 <= x < h and 0 <= y < w:
                dp[i][j] += dp[x][y]
                dp[i][j] %= mod

print(dp[-1][-1])