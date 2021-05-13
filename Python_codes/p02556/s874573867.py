# -*- coding: utf-8 -*-
# モジュールのインポート
import sys

# 標準入力を取得
N = int(input())
x, y = [], []
for i in range(N):
    x_i, y_i = list(map(int, input().split()))
    x.append(x_i)
    y.append(y_i)

# 求解処理
max_z = -sys.maxsize
min_z = sys.maxsize
max_w = -sys.maxsize
min_w = sys.maxsize
for x_i, y_i in zip(x, y):
    z_i = x_i + y_i
    max_z = max(max_z, z_i)
    min_z = min(min_z, z_i)
    w_i = x_i - y_i
    max_w = max(max_w, w_i)
    min_w = min(min_w, w_i)
ans = max(max_z - min_z, max_w - min_w)

# 結果出力
print(ans)
