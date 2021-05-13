n, m = map(int, input().split())
r = [2**i for i in range(n+1)]

price = [0] * m
mask = [0] * m
for i in range(m):
    a, b = map(int, input().split())
    for box in map(int, input().split()):
        mask[i] += r[box-1]
    price[i] = a


inf = 10**9
dp = [[inf] * (1 << n) for _ in range(m+1)]
dp[0][0] = 0
for i in range(m):
    for j in range(1 << n):
        dp[i+1][j | mask[i]] = min(
            dp[i][j] + price[i],
            dp[i+1][j | mask[i]]
        )
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])

ans = dp[m][(1 << n) - 1]
if ans == inf:
    print(-1)
else:
    print(ans)
