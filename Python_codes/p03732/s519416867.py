import sys
input = sys.stdin.readline

N,W = map(int,input().split())
info = []
for i in range(N):
    w,v = map(int,input().split())
    if i == 0:
        w1 = w
    w = w - (w1-1)
    info.append((w,v))
# dp[i][j][k]
# dp[i][j][k] = max(dp[i-1][j][k],dp[i-1][j-w][k-1])
# dp[0][j][0] = 0
# ans = max(dp[N][j][k] w1*k + j <= W)
dp = [[[0]*(N+1) for _ in range(400)] for _ in range(N+1)]
for i in range(1,N+1):
    w = info[i-1][0]; v = info[i-1][1]
    for j in range(400):
        for k in range(1,N+1):
            dp[i][j][k] = dp[i-1][j][k]
            if j - w >= 0:
                if dp[i][j][k] < dp[i-1][j-w][k-1] + v:
                    dp[i][j][k] = dp[i-1][j-w][k-1] + v
ans = -1
for j in range(400):
    for k in range(N+1):
        if not((w1-1)*k + j <= W):
            continue
        if dp[N][j][k] > ans:
            ans = dp[N][j][k]
print(ans)