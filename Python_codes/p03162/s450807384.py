N = int(input())
dp = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    ipt = list(map(int, input().split()))
    for j in range(3):
        if j != 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][0] + ipt[j])
        if j != 1:
            dp[i][j] = max(dp[i][j], dp[i - 1][1] + ipt[j])
        if j != 2:
            dp[i][j] = max(dp[i][j], dp[i - 1][2] + ipt[j])

print(max(dp[N][0], dp[N][1], dp[N][2]))
