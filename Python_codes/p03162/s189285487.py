N = int(input())
dp = [[0, 0, 0] for _ in range(N + 1)]

for i in range(1, N+1):
    a = list(map(int, input().split()))
    for j in range(3):
        dp[i][j] = a[j] + max(dp[i - 1][(j+1) % 3], dp[i - 1][(j+2) % 3])

print(max(dp[N]))