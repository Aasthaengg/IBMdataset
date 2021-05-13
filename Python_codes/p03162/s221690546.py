import sys
# inputを高速化する。
input = sys.stdin.readline
# 入力
vacation = int(input())
lst_happiness = [list(map(int, input().split())) for i in range(vacation)]
# DPテーブル
# 最大化問題なので0で初期化
dp = [[0 for i in range(3)] for j in range(vacation+1)]
def chmax(a, b):
    if a > b:
        return a
    else:
        return b
# dp[i][0] から dp[i + 1][1] への遷移
# dp[i][0] から dp[i + 1][2] への遷移
# dp[i][1] から dp[i + 1][0] への遷移
# dp[i][1] から dp[i + 1][2] への遷移
# dp[i][2] から dp[i + 1][0] への遷移
# dp[i][2] から dp[i + 1][1] への遷移
# 各 j (= 0, 1, 2) と各 k (= 0, 1, 2) に対して、j ≠ k ならば
# chmin(dp[i + 1][k], dp[i [j] + lst_happiness[i][k])
for i in range(vacation):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][k] = chmax(dp[i+1][k], dp[i][j] + lst_happiness[i][k])
ans = 0
for i in range(3):
    ans = chmax(ans, dp[vacation][i])
print(ans)