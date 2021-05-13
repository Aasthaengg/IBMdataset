import sys
input = sys.stdin.readline
#import math
#import numpy as np
N = int(input())
#= input()
#= map(int, input().split())
p = list(map(float, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= {i:[] for i in range(N)}

dp = [[0.0] * (N + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i, p in enumerate(p, 1):
    pp = 1 - p
    dpi = dp[i - 1]
    for j in range(i + 1):     
        if j == 0:
            dp[i][j] = dpi[j] * pp
        elif j == i:
            dp[i][j] = dpi[j - 1] * p
        else:
            dp[i][j] = dpi[j - 1] * p + dpi[j] * pp


res = 0.0
n = N // 2 + 1

for cnt in dp[-1][n:]:
    res += cnt

print(res)