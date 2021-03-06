#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
H = list(map(int, input().split()))

dp = [10**9] * N
dp[0] = 0
for i in range(N - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i + 1] - H[i]))
    
    if i < N - 2:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i + 2] - H[i]))

print(dp[-1])