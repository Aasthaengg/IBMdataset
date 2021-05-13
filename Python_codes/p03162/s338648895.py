N = int(input())
a1, b1, c1 = map(int, input().split())
dp = [[0, 0, 0] for _ in range(N)]
dp[0][0] = a1
dp[0][1] = b1
dp[0][2] = c1
for i in range(1, N):
    a, b, c = map(int, input().split())
    dp[i][0] = a + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = b + max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = c + max(dp[i-1][0], dp[i-1][1])

print(max(dp[-1]))
