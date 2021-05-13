import sys
input = sys.stdin.readline

N, W = map(int, input().split())
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())
w0 = w[0]
for i in range(N):
    w[i] -= w0
s = sum(w)
dp = [[-1] * (s+1) for _ in range(N+1)]
dp[0] = [0] * (s+1)
for n in range(N):
    for i in range(N)[::-1]:
        for j in range(s-w[n]+1)[::-1]:
            if dp[i][j] == -1:
                continue
            dp[i+1][j+w[n]] = max(dp[i+1][j+w[n]], dp[i][j] + v[n])
ans = 0
for i in range(N+1):
    if W - w0 * i >= 0:
        ans = max(ans, dp[i][min(s, W-w0*i)])
print(ans)
