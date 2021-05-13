ans = 10 ** 7
n, m = map(int, input().split())
dp = [float('inf')] * (2 ** n)
dp[0] = 0
prices = []
for i in range(m):
    a, s = map(int, input().split())
    prices.append(a)
    f = 0
    for k in map(int, input().split()):
        f += 2 ** (k - 1)
    for j in range(2 ** n - 1, -1, -1):
        dp[j | f] = min(dp[j] + a, dp[j | f])
print(-1 if dp[-1] == float('inf') else dp[-1])