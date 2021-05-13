N = int(input())

p_list = list(map(float, input().split()))

dp = [[0.0] * (N+1) for i in range(N+1)]
dp[0][0] = 1.0

for i in range(N):
    for j in range(i+1):
        dp[i+1][j+1] += dp[i][j] * p_list[i]
        dp[i+1][j] += dp[i][j] * (1.0 - p_list[i])
    #print(dp[i])

ans = 0
for j in range(N//2+1, N+1):
    ans += dp[N][j]
#print(dp)
print(ans)