import numpy as np

H, W = map(int,input().split())
#A = [input() for _ in range(H)]
A = np.array([list(input()) for _ in range(H)], 'U1')
mod = 10**9+7

eq = A == '.'

dp = [[0 for j in range(W+1)] for i in range(H+1)]
dp[0][1] = 1

for i in range(H):
    for j in range(W):
        if eq[i][j]:
            dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j]) % mod

print(dp[-1][-1])
