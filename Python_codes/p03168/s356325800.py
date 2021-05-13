N = int(input())
p_list = list(map(float, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    for j in range(i+1):
        dp[i][j] += dp[i-1][j] * (1-p_list[i-1])
        if j > 0:
            dp[i][j] += dp[i-1][j-1] * p_list[i-1]
ans = 0       
start = N//2 + 1
for p in dp[N][start:]:
    ans += p
print(ans)