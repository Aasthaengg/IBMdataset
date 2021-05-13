H, N = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]

dp = [float("INF")] * (H+1)
dp[0] = 0  # 添字：敵HP、　配列の中身：敵HPを削るのに必要な最小のMP

# 配るDP
for h in range(H):
    for a, b in ab:
        target = min(H, h + a)  # target: DPのうち、書き換える部分の添字。Hを超えた部分は考察する必要なし
        dp[target] = min(dp[target], dp[h] + b)

print(dp[-1])