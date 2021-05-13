import sys
input = sys.stdin.readline

N, W = [int(x) for x in input().split()]
wv = []
for _ in range(N):
    wv.append([int(x) for x in input().split()])
w1 = wv[0][0]
dp = [[[0] * (N + 1) for _ in range(4 * N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = wv[i - 1]
    w -= (w1 - 1)
    for j in range(4 * N + 1):
        for k in range(1, N + 1):
            if j - w >= 0:
                dp[i][j][k] = max(dp[i - 1][j - w][k - 1] + v, dp[i - 1][j][k])
            else:
                dp[i][j][k] = dp[i - 1][j][k]
ans = 0
for i in range(N + 1):
    for j in range(4 * N + 1):
        for k in range(N + 1):
            if W - (w1 - 1) * k >= j:
                ans = max(ans, dp[i][j][k])

print(ans)
