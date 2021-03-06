import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
inf = 999999999

n = int(input())
h = list(map(int, input().split()))

dp = [inf] * (n + 1)
dp[0] = 0
for i in range(0, n - 1):
    cost = abs(h[i + 1] - h[i])
    dp[i + 1] = min(dp[i + 1], dp[i] + cost)
    if i + 2 < n:
        cost = abs(h[i + 2] - h[i])
        dp[i + 2] = min(dp[i + 2], dp[i] + cost)

print(dp[n - 1])
