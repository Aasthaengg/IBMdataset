N = int(input())
p = list(map(float, input().split()))

# i-1 まで見たときに表が j 枚出る確率
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    for j in range(N+1):
        dp[i][j] += (1-p[i-1])*dp[i-1][j]
        if j >= 1:
            dp[i][j] += p[i-1]*dp[i-1][j-1]

print(sum([dp[N][N-j] for j in range((N+1)//2)]))