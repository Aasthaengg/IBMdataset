# https://atcoder.jp/contests/abc099/tasks/abc099_c

# DPを考えてみる
# dp[i]: i円を引き出すのに必要な回数
# dp[0] = 1
# dp[1] = 1
# dp[6] の倍数 = 1
# dp[9] の倍数 = 1

# 10万以下でありえる値
# 6**7 # 279936
# 9**6 # 531441
c = [1] + [6**i for i in range(1,7)] + [9**i for i in range(1,6)]

Inf = int(1e18)

n = int(input())
dp = [Inf] * (n + 1)
dp[0] = 0

# 金額毎
for ci in c:
    for i in range(ci, n+1):
        # ある金額のminは，その金額を降ろさないmin + 1回
        # 1000円でc=9の場合，dp[1000] = min(dp[1000], dp[1000-9]+ 1)
        dp[i] = min(dp[i], dp[i-ci] + 1)

print(dp[n])