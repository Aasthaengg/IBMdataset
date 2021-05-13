import copy
import heapq
H, W = map(int, input().split())
S = [['.'] * (W+1)]
for _ in range(H):
    s = list(input())
    s.insert(0,'.')
    S.append(s)

inf = float('inf')

dp = []
for _ in range(H+1):
    dp.append([inf] * (W+1))

if S[1][1] == '.':
    dp[1][1] = 0
else:
    dp[1][1] = 1

for i in range(1,H+1):
    for j in range(1,W+1):
        right = dp[i][j-1]
        down = dp[i-1][j]
        if S[i][j] == '#':
            if S[i-1][j] == '.':
                down += 1
            if S[i][j-1] == '.':
                right += 1

        dp[i][j] = min(dp[i][j],right,down)

print(dp[H][W])