N , W = map(int,input().split())
mono = [tuple(map(int,input().split())) for i in range(N)]
w1 = mono[0][0]
dp = [[-1 for i in range(301)] for j in range(N+1)]
dp[0][0] = 0 

for i in range(N):
    p = mono[i][0] - w1
    for j in reversed(range(N)):
        for k in reversed(range(301)):
            if dp[j][k] != -1:
                dp[j+1][k+p] = max(dp[j+1][k+p],dp[j][k]+mono[i][1])

ans = 0
for i in range(N+1):
    for j in range(301):
        if i*w1 + j <= W:
            ans = max(ans,dp[i][j])

print(ans)