import sys
sys.setrecursionlimit(10000000)

n = int(input())
h = list(map(int, input().split()))

def chmin(a, b):
    if a > b: return b
    else: return a

def rec(i):
    if dp[i] < float('inf'): return dp[i]
    
    if i == 0: return 0

    res = float('inf')
    res = chmin(res, rec(i - 1) + abs(h[i] - h[i - 1]))
    if i > 1:
        res = chmin(res, rec(i - 2) + abs(h[i] - h[i - 2]))
    dp[i] = res
    return dp[i]

dp = [float('inf')] * n
print(rec(n - 1))