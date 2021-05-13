# -*- coding: utf-8 -*-
import math

# import copy


# 引数が一つだけのやつ
n = int(input())
# 引数が複数あるやつ（全部数字）
target_1 = [int(x) for x in input().split()]

# 引数が複数あるやつ（そうじゃないの）
# target = [int(x) for x in input().split()]

# number = int(input())
# 複数行を受け取って処理するやつ
# target = [list(input()) for i in range(H)]

# 関数
def count_sharp(target):
    return sum([x.count("#") for x in target])


def bin_code(value, keta):
    return list(("{:0" + str(keta) + "b}").format(value))


# 初期
target_1.sort()
point = 0
for idx, ins in enumerate(target_1):
    if idx != len(target_1) - 1:
        point += target_1[-1 - math.ceil(idx / 2)]

# 出力
print(point)
