# -*- coding: utf-8 -*-
# 引数が一つだけのやつ
# n = int(input())
# 引数が複数あるやつ（全部数字）
# target = [int(x) for x in input().split()]

# 引数が複数あるやつ（そうじゃないの）
# target = [int(x) for x in input().split()]

# 最初の行で複数行を受け取って処理するやつ
target_1 = list(input())
target_2 = list(input())

# 初期

result = 0
# 判定
for idx in range(len(target_1)):
    if target_1[idx] != target_2[idx]:
        result += 1

print(result)
