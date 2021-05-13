import sys
input = sys.stdin.readline
from collections import *

N, P = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0]*2 for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    if A[i]%2==0:
        dp[i+1][0] = 2*dp[i][0]
        dp[i+1][1] = 2*dp[i][1]
    else:
        dp[i+1][0] = dp[i][0]+dp[i][1]
        dp[i+1][1] = dp[i][0]+dp[i][1]

print(dp[N][P])