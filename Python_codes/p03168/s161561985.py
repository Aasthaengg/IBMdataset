import numpy as np
import sys
input = sys.stdin.readline

N = int(input())
p0_list = np.array([float(item) for item in input().split()])
p1_list = 1 - p0_list

dp = np.zeros((N+1, N+1), dtype='float')
dp[0, 0] = 1

for i in range(N):
    dp[i+1][:-1] += dp[i][:-1] * p1_list[i]
    dp[i+1][1:]  += dp[i][:-1] * p0_list[i]

print(np.sum(dp[N, (N+1)//2:]))
