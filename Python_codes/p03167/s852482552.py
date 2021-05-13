import sys
def input(): return sys.stdin.readline().rstrip()
H, W = map(int, input().split())
a = [list(input()) for i in range(H)]
dp = [[0]*(W+1) for i in range(H+1)]
dp[0][1] = 1
mod = 10**9 + 7
for i in range(1, H+1):
    for j in range(1, W+1):
        if a[i-1][j-1] == ".":
            dp[i][j] += dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= mod
            
ans =dp[H][W]
print(ans)