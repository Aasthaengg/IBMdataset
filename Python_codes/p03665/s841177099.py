N, P = map(int, input().split(' '))
A = tuple(map(int, input().split(' ')))

dp = [[0, 0] for _ in range(N + 1)]
dp[0][0] = 1

for index, a in enumerate(A, start=1):
    if a % 2 == 0:
        dp[index][0] = dp[index - 1][0] * 2
        dp[index][1] = dp[index - 1][1] * 2
    else:
        dp[index][0] = dp[index - 1][1] + dp[index - 1][0]
        dp[index][1] = dp[index - 1][0] + dp[index - 1][1]

print(dp[N][P])
