N, Ma, Mb = map(int, input().split())
Items = [list(map(int, input().split())) for _ in range(N)]

# dp[i][a][b] := i番目の薬品までみて、タイプA: xグラム, タイプB: yグラム を手に入れるために必要な最小費用
dp = [[[float('inf')] * 401 for j in range(401)] for i in range(N + 1)]
dp[0][0][0] = 0
for i, (a, b, c) in enumerate(Items):
    for x in range(401):
        for y in range(401):
            dp[i + 1][x][y] = min(dp[i + 1][x][y], dp[i][x][y])
            if x + a > 400 or y + b > 400:
                continue
            dp[i + 1][x + a][y + b] = min(dp[i + 1][x + a][y + b], dp[i][x][y] + c)

ans = float('inf')
i = 1
while Ma * i <= 400 and Mb * i <= 400:
    ans = min(ans, dp[-1][Ma * i][Mb * i])
    i += 1
print(ans if ans != float('inf') else -1)
