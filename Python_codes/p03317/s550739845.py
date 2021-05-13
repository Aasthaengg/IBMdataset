# -*- coding: utf-8 -*-
# モジュールのインポート
import math

# 標準入力を取得
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 求解処理
x = A.index(1)
y = N - x - 1
ans = math.ceil(x / (K - 1))
if x % (K - 1) != 0:
    y -= K - 1 - (x % (K - 1))
ans += math.ceil(y / (K - 1))

# 結果出力
print(ans)
