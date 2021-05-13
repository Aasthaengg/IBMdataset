n,W = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

dp = {}
dp[0] = 0
for w, v in a:
    pre_dp = dp.copy()
    for pw, pv in pre_dp.items():
        if pw + w <= W:
            dp[pw + w] = max(dp.get(pw + w, 0), pv + v)

print(max(dp.values()))