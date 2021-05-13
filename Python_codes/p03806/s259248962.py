n, ma, mb = map(int, input().split())

item = [tuple(map(int, input().split())) for _ in range(n)]

INF = 5000
dp = [[INF] * 444 for _ in range(444)]


dp[0][0] = 0

for i in range(n):
    next = [[INF] * 444 for _ in range(444)]
    for j in range(401):
        for k in range(401):
            a, b, c = item[i]
            next[j + a][k + b] = min(next
                                     [j + a][k + b], dp[j][k] + c)
            next[j][k] = min(next[j][k], dp[j][k])
    dp = next

ans = INF
for i in range(1, 401):
    for j in range(1, 401):  # i : j == ma : mb
        if ma * j == i * mb:
            ans = min(ans, dp[i][j])
print(ans if ans != INF else -1)
