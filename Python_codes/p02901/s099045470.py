n, m = map(int, input().split())
can_open = []
cost = []
for _ in range(m):
    a, b = map(int, input().split())
    cost.append(a)
    it = map(int, input().split())
    x = 0
    for c in it:
        x += 1 << (c-1)
    can_open.append(x)

n_bit = 1 << n
INF = 10**18
dp = [[INF]*(m+1) for _ in range(n_bit)]
dp[0][0] = 0

for j in range(n_bit):
    for i in range(m):
        dp[j][i+1] = min(dp[j][i+1], dp[j][i])
        dp[j | can_open[i]][i +
                            1] = min(dp[j | can_open[i]][i+1], dp[j][i+1]+cost[i])

print(dp[-1][-1] if dp[-1][-1] != INF else -1)
