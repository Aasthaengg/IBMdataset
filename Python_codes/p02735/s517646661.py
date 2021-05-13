import sys
input = sys.stdin.readline
from collections import *

H, W = map(int, input().split())
s = [input()[:-1] for _ in range(H)]
dp = [[10**18]*W for _ in range(H)]

if s[0][0]=='.':
    dp[0][0] = 0
else:
    dp[0][0] = 1
    
for i in range(H):
    for j in range(W):
        if i>0:
            if s[i-1][j]=='.' and s[i][j]=='#':
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
        
        if j>0:
            if s[i][j-1]=='.' and s[i][j]=='#':
                dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[-1][-1])