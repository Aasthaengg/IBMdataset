import sys
sys.setrecursionlimit(10**6)

N = int(input())
h = list(map(int, input().split()))
dp = [-1] * (N+1)

def rec(i):
    if i == 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    dp[i] = 2**60 # 十分大きな値
    if i - 1 >= 0:
        dp[i] = min(dp[i], rec(i - 1) + abs(h[i - 1] - h[i]))
    if i - 2 >= 0:
        dp[i] = min(dp[i], rec(i - 2) + abs(h[i - 2] - h[i]))
    return dp[i]

print(rec(N-1))
