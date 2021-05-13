n, m = map(int, input().split())
key = []
for _ in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    v = 0
    for i in range(b):
        v += 1 << (c[i] - 1)
    key.append([a, v])

dp = [[float('inf')] * (1<<n) for _ in range(m+1)]
dp[0][0] = 0
for i in range(m):
    money, value = key[i]
    for j in range(1<<n):
        dp[i+1][j|value] = min(dp[i+1][j|value], dp[i][j] + money)
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

print(dp[-1][-1] if dp[-1][-1] != float('inf') else -1)