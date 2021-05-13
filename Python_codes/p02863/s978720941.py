N, T = map(int, input().split())
a_list = []
for _ in range(N):
    a, b = map(int, input().split())
    a_list.append((a, b))
a_list.sort(key=lambda x: x[0])

dp = [[0 for _ in range(T + 3001)] for _ in range(N + 1)]
for i in range(1, N + 1):
    a, b = a_list[i - 1]
    for j in range(T + 3001):
        dp[i][j] = dp[i - 1][j]
    for j in range(T):
        dp[i][j + a] = max(dp[i - 1][j + a], dp[i - 1][j] + b)
print(max(dp[-1]))