import sys
input = sys.stdin.readline
n, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()

dp = [[0 for j in range(t+1)] for i in range(n+1)]

for i in range(n):
    for j in range(t+1):
        dp[i+1][j] =  dp[i][j]
    for j in range(t):
        next = min(j + ab[i][0], t)
        dp[i+1] [next] = max(dp[i+1][next], dp[i][j] + ab[i][1])
print(max(dp[n]))
