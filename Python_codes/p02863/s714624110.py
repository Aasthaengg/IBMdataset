n, t = map(int, input().split())
dp1 = [[-float("inf") for i in range(t)] for i in range(n + 1)]
dp1[0][0] = 0
dp2 = [[-float("inf") for i in range(t)] for i in range(n + 1)]
dp2[n][0] = 0
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))
for i in range(n):
    a, b = ab[i]
    for j in range(t - 1, -1, -1):
        if j >= a:
            dp1[i + 1][j] = max(dp1[i][j], dp1[i][j - a] + b)
        else:
            dp1[i + 1][j] = dp1[i][j]
for i in range(n + 1):
    for j in range(t - 1):
        dp1[i][j + 1] = max(dp1[i][j], dp1[i][j + 1])
for i in range(n - 1, -1, -1):
    a, b = ab[i]
    for j in range(t - 1, -1, -1):
        if j >= a:
            dp2[i][j] = max(dp2[i + 1][j], dp2[i + 1][j - a] + b)
        else:
            dp2[i][j] = dp2[i + 1][j]
for i in range(n + 1):
    for j in range(t - 1):
        dp2[i][j + 1] = max(dp2[i][j], dp2[i][j + 1])
ans = [max([dp1[i][j] + dp2[i + 1][t - 1 - j] + ab[i][1] for j in range(t)]) for i in range(n)]
print(max(ans))