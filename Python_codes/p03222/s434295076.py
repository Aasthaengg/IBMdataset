import sys
input = sys.stdin.readline
mod = 10**9 + 7

h, w, k = [int(x) for x in input().split()]

dp = [[0]*w for _ in range(h + 1)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        x = 0 # right
        y = 0 # left
        z = 0 # remain
        for l in range(2**(w - 1)):
            l = bin(l)[2:].zfill(w - 1)
            if "11" in l:
                continue
            if j - 1 >= 0 and l[j - 1] == "1":
                y += 1
            elif j + 1 < w and l[j] == "1":
                x += 1
            else:
                z += 1
        if j + 1 < w:
            dp[i + 1][j + 1] += x * dp[i][j]
            dp[i + 1][j + 1] %= mod
        if j - 1 >= 0:
            dp[i + 1][j - 1] += y * dp[i][j]
            dp[i + 1][j - 1] %= mod
        dp[i + 1][j] += z * dp[i][j]
        dp[i + 1][j] %= mod

print(dp[-1][k - 1])
            
            
