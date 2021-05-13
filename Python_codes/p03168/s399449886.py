N = int(input())
P = list(map(float, input().split()))
dp = [[0]*(N+1) for _ in range(N)]
dp[0][0] = 1-P[0]
dp[0][1] = P[0]
for i in range(N):
    for k in range(N+1):
        if i-1 >= 0:
            dp[i][k] += dp[i-1][k]*(1-P[i])
            if k-1 >= 0:
                dp[i][k] += dp[i-1][k-1]*P[i]
ans = 0
for i in range(N+1):
    if i >= (-(-N//2)):
        ans += dp[-1][i]
print(ans)
