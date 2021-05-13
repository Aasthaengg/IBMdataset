import sys
sys.setrecursionlimit(10**7)

N = int(input())
h = list(map(int, input().split()))

dp = [-1] * N

# 足場 i から 足場 N - 1 まで移動するときのコストの最小値
def rec(i):
    if dp[i] >= 0:
        return dp[i]
    
    res = -1
    if i == N - 1:
        res = 0
    elif i == N - 2:
        res = rec(i + 1) + abs(h[i + 1] - h[i])
    else:
        res =  min(rec(i + 1) + abs(h[i + 1] - h[i]), rec(i + 2) + abs(h[i + 2] - h[i]))
    
    dp[i] = res
    return dp[i]

print(rec(0))