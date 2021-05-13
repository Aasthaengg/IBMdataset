import sys
import numpy as np

def input():
    return sys.stdin.readline()[:-1]
  
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7

H, W = map(int,input().split())
#A = [list(map(int,input().split())) for _ in range(H)]
A = np.array([list(input()) for _ in range(H)], 'U1')
eq = A == '.'

dp = np.zeros(W+1, dtype=int)
dp[1] = 1

for i in range(1,H+1):
    prev = dp.copy()
    for j in range(1,W+1):
        if eq[i-1][j-1]:
            dp[j] = prev[j] + dp[j-1]
        else:
            dp[j] = 0
    dp %= mod

print(dp[-1])