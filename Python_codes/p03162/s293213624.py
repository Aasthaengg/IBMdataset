N = int(input())
abc = [list(map(int, input().split())) for i in range(N)]

dp = [[abc[0][0], abc[0][1], abc[0][2]]] + [[0, 0, 0] for i in range(N - 1)]

for i in range(1, N):
    dp[i][0] = abc[i][0] + max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = abc[i][1] + max(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = abc[i][2] + max(dp[i - 1][0], dp[i - 1][1])
print(max(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))
