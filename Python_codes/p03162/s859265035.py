N = int(input())
event = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N)]
dp[0] = event[0]

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + event[i][j])
print(max(dp[N - 1]))
