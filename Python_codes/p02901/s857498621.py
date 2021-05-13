n, m = map(int, input().split())
INF = 10 ** 5 * 12
dp = [INF] * (1 << n)
dp[0] = 0
keys = []

for _ in range(m):
    a, b = map(int, input().split())
    s = 0
    for c in list(map(int, input().split())):
        s |= 1 << (c - 1)
    keys.append([s, a])

for s in range(1 << n):
    for i in range(m):
        to = s | keys[i][0]
        cost = dp[s] + keys[i][1]
        dp[to] = min(dp[to], cost)

ans = dp[-1] if dp[-1] != INF else -1
print(ans)
