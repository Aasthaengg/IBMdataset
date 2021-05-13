N = int(input())
A = list(map(int, input().split()))

D = [(A[i], i) for i in range(N)]
D.sort(reverse=True)

dp = [[0 for j in range(N + 1)] for i in range(N + 1)]

for j in range(1, N + 1):
    dp[0][j] = dp[0][j - 1] + D[j - 1][0] * abs(D[j - 1][1] - (N - j))

for i in range(1, N + 1):
    dp[i][0] = dp[i - 1][0] + D[i - 1][0] * abs(D[i - 1][1] - (i - 1))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i + j > N:
            continue
        dp[i][j] = max(dp[i][j - 1] + D[i + j - 1][0] * abs(D[i + j - 1][1] - (N - j)), dp[i - 1][j] + D[i + j - 1][0] * abs(D[i + j - 1][1] - (i - 1)))

res = 0

for i in range(N + 1):
    for j in range(N + 1):
        if i + j == N:
            res = max(res, dp[i][j])

print(res)