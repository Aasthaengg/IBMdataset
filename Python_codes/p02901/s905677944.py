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
dp = [INF]*n_bit
dp[0] = 0

for i in range(m):
    for j in range(n_bit):
        dp[j | can_open[i]] = min(dp[j | can_open[i]], dp[j]+cost[i])

print(dp[-1] if dp[-1] != INF else -1)