#!/usr/bin/env python3
import sys
input = sys.stdin.readline

R, C, k = map(int, input().split())
field = [[0] * C for _ in range(R)]
for _ in range(k):
    r, c, v = map(int, input().split())
    r -= 1; c -= 1
    field[r][c] = v

# dp[taken 0 - 2][R][C]
dp = [[-1] * (C + 1) * (R + 1) for _ in range(4)]
dp0 = dp[0]; dp1 = dp[1]; dp2 = dp[2]; dp3 = dp[3]
dp[0][0] = 0
for j in range(C):
    for i in range(R):
        ij = i * C + j
        ij1 = ij + 1
        i1j = ij + C
        item = field[i][j]
        # Use
        if item:
            dp1[ij1] = max(dp1[ij1], dp0[ij] + item) 
            dp0[i1j] = max(dp0[i1j], dp0[ij] + item) 
        dp0[i1j] = max(dp0[i1j], dp0[ij]) 
        dp0[ij1] = max(dp0[ij1], dp0[ij]) 
        if item:
            dp2[ij1] = max(dp2[ij1], dp1[ij] + item) 
            dp0[i1j] = max(dp0[i1j], dp1[ij] + item) 
        dp0[i1j] = max(dp0[i1j], dp1[ij]) 
        dp1[ij1] = max(dp1[ij1], dp1[ij]) 
        if item:
            dp3[ij1] = max(dp3[ij1], dp2[ij] + item) 
            dp0[i1j] = max(dp0[i1j], dp2[ij] + item) 
        dp0[i1j] = max(dp0[i1j], dp2[ij]) 
        dp2[ij1] = max(dp2[ij1], dp2[ij]) 
        dp0[i1j] = max(dp0[i1j], dp3[ij]) 
        dp3[ij1] = max(dp3[ij1], dp3[ij]) 

ans = 0
for i in range(4):
    for j in range(R + 1):
        ans = max(ans, dp[i][j * C + C - 1])
print(ans)