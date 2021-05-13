H,W = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(10)]
A = [list(map(int,input().split())) for _ in range(H)]
dp = [float("INF")]*(10)
dp[1] = 0
cnt = 1
while cnt < 10:
    cnt += 1
    for i in range(10):
        for j in range(10):
            dp[i] = min(dp[i],dp[j]+C[i][j])
ans = 0
for i in range(H):
    for j in range(W):
        a = A[i][j]
        if a != -1:
            ans += dp[a]
print(ans)

