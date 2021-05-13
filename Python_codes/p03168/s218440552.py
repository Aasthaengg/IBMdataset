N = int(input())
P = list(map(float, input().split()))
dp = [[0]*(N+1) for i in range(N+1)]
dp[0][0] = 1
# dp[X][I] := X回目の操作を終えてi回面が出る確率
for i in range(1, N+1):
    p = P[i-1]
    for j in range(i+1):
        if j >= 1:
            dp[i][j] = dp[i-1][j]*(1-p) + dp[i-1][j-1]*p
        else:
            dp[i][j] = dp[i-1][j]*(1-p)
ans = 0
for i in range(N//2+1, N+1):
    ans += dp[N][i]
print(ans)
