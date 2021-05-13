N, W = [int(_) for _ in input().split()]
WV = [[int(_) for _ in input().split()] for _ in range(N)]
dp = {}
dp[0] = 0
for weight, value in WV:
    dp_old = dp.copy()
    for k, v in dp_old.items():
        if k + weight <= W:
            dp[k + weight] = max(dp.get(k + weight, 0), v + value)
ans = 0
for k, v in dp.items():
    ans = max(ans, v)
print(ans)
