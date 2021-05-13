# -*- coding: utf-8 -*-
# 標準入力を取得
n = int(input())

# 求解処理
# dp[i+1]: フィボナッチ数列の第i項
dp = [0 for _ in range(n + 1)]

# 初期条件
dp[0] = 1
dp[1] = 1

for i in range(1, n):
    # DP漸化式
    dp[i + 1] = dp[i] + dp[i - 1]
ans = dp[n]

# 結果出力
print(ans)
