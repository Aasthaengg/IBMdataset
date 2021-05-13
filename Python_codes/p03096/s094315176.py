from collections import defaultdict

MOD = 10 ** 9 + 7

N = int(input())
c = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N + 1)]
dp[0] = 1
# dp[index] = 場合の数
# 1-indexed

d = defaultdict(lambda: -1)
# d[色] = index
# 指定色が直前に出現した位置
# 1-indexed

for i, cc in enumerate(c, 1):
    dp[i] = dp[i - 1]
    # 手前までの塗り方に
    # i番目の石をつなげたパターン
    # dp[i - 1] = 手前までの色の塗り方
    if 1 <= d[cc] < i - 1:
        # 指定色が出現している場合
        # （出現なし -> -1）
        dp[i] += dp[d[cc]]
        # 直前の指定色からi番目の石までの区間を色変更したパターン
        # dp[d[cc]] = 直前の指定色までの色の塗り方
    dp[i] %= MOD
    d[cc] = i
    # print(d)
    # print(dp)
print(dp[N])