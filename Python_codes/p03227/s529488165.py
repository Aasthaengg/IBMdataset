# -*- coding: utf-8 -*-

# 入力値受け取り
S = input()

if len(S) == 3:
    S = S[::-1]

# 結果出力
print("{}".format(S))
