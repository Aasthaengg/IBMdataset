import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    A = list(map(int,input().split()))
    AI = [(a, i) for i, a in enumerate(A)]
    AI.sort(reverse = 1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for l in range(n):
        for r in range(n):
            if l + r >= n:
                break
            a, i = AI[l + r]
            dp[l + 1][r] = max(dp[l + 1][r], dp[l][r] + abs(i - l) * a)
            dp[l][r + 1] = max(dp[l][r + 1], dp[l][r] + abs((n - r - 1) - i) * a)
    print(max(dp[i][n - i] for i in range(n)))
resolve()