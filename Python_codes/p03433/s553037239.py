# -*- coding: utf-8 -*-
# 標準入力の取得
N = int(input())
A = int(input())

# 求解処理
result = str()
if (N % 500) <= A:
    result = "Yes"
else:
    result = "No"

# 結果出力
print(result)
