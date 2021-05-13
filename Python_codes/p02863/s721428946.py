N, T = map(int, input().split())
K = []
for i in range(N):
    a, b = map(int, input().split())
    K.append([a, b])
K.sort()

dp = [[0]*(N+1) for _ in range(T+3001)]

for i in range(1, T+3001):
    for j in range(N):
        if 0 <= i - K[j][0] <= T-1:
            dp[i][j+1] = max(dp[i - K[j][0]][j]+K[j][1], dp[i][j])
        else:
            dp[i][j+1] = dp[i][j]

ans = 0
for i in range(1,T+3001):
    ans = max(dp[i][N],ans)
print(ans)