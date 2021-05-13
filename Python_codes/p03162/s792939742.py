N = int(input())
dp = [[0, 0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    a = tuple(map(int, input().split()))
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + a[j])
print(max(dp[N]))