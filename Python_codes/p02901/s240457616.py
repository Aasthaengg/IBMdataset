n, m = map(int, input().split())
ac = []
for _ in range(m):
    ai, bi = map(int, input().split())
    ci = list(map(lambda x: 2 ** (int(x) - 1) , input().split()))
    ac.append((ai, sum(ci)))

INF = 100 ** 18
dp = [INF] * (2**n)
dp[0] = 0
for ai, ci in ac:
    for j in range(0, 2**n):
        dp[j | ci] = min(dp[j | ci], dp[j] + ai)

ans = dp[2**n-1]
if ans == INF:
    print(-1)
    exit()
print(ans)

