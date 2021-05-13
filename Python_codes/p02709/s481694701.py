from bisect import bisect_left
N = int(input())
As = [(x, i) for i, x in enumerate(map(int, input().split()))]

up = sorted(As)
dp = [[0]*(N+1) for _ in range(N+1)]

for i, (u, idx) in enumerate(up[::-1], 1):
    for j in range(i):
        left = j
        right = N-(i-j)
        dp[i][j] = max(dp[i][j], dp[i-1][j]+u*abs(right-idx))
        dp[i][j+1] = max(dp[i][j+1], dp[i-1][j]+u*abs(left-idx))

print(max(dp[-1]))