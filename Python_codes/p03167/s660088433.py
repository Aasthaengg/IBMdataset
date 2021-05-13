
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

H,W = map(int,input().split())
A = [input() for _ in range (H)]

MOD = 10**9+7
dp = [[0] * (W+1) for _ in range(H+1)]
dp[0][0] = 1
dp[1][1] = 1
for i in range(H):
    for j in range(W):
        if i==j and i==0:continue
        if A[i][j]=='.':
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
            dp[i+1][j+1] %= MOD

print(dp[H][W])