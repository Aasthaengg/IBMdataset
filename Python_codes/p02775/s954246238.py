import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = list(map(int, input()))

def solve(N):
    dp = (0, 1) # n円の場合とn+1円の場合
    for n in N:
        a = min(dp[0] + n, dp[1] + 10 - n)
        b = min(dp[0] + n + 1, dp[1] + 10 - (n+1))
        dp = (a, b)
    return dp[0]

print(solve(N))
