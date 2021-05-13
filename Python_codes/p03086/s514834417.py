# -*- coding: utf-8 -*-
# 標準入力を取得
S = input()

# 求解処理
ACGT = ["A", "C", "G", "T"]
ans = 0
N = len(S)
for i in range(N):
    for j in range(i, N):
        if all([S[k] in ACGT for k in range(i, j + 1)]):
            ans = max(ans, j - i + 1)

# 結果出力
print(ans)