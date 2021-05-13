
N, K = map(int, input().split())
X = list(map(int, input().split()))

lim = 100
dp = [[0] * (N + 1) for _ in range(lim)]
dp[0] = [0] + X
for k in range(1, lim):
    for i in range(N + 1):
        dp[k][i] = dp[k - 1][dp[k - 1][i]]

ans = 1
for i in range(lim):
    if K >> i & 1:
        ans = dp[i][ans]

print(ans)
