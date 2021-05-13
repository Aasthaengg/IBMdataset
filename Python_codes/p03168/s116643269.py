import sys 
input = sys.stdin.readline

n = int(input())
p = [float(x) for x in input().split()]

dp = [[0]*(n + 1) for _ in range(n + 1)]
dp[0][0] = 1

ans = 0

for i in range(1, n + 1):
    p_i = p[i - 1]
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j] * (1 - p_i)
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1] * (p_i)
        if i == n and j > (i - j):
            ans += dp[i][j]

print(ans)
