H,W = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(10)]
A = [list(map(int,input().split())) for _ in range(H)]
dp = [float("INF")]*(10)
dp[1] = 0
cnt = 0
while cnt <= 10:
    cnt += 1
    for i in range(10):
        for j in range(10):
            dp[j] = min(dp[j],dp[i]+C[j][i])

cost = 0
for i in range(H):
    for j in range(W):
        if A[i][j] != -1:
            cost += dp[A[i][j]]
print(cost)