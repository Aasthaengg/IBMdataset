# https://atcoder.jp/contests/abc144/tasks/abc144_d

import math
a, b, x = map(int, input().split())

# 高さ
y = x / (a ** 2)

if y >= ((1 / 2) * b):
    d = math.atan2(2 * (y * a - a * b), a ** 2)

    # dを度数法単位に変換
    d_deg = math.degrees(d)

    print(abs(d_deg))

else:
    d = math.atan2((1 / 2) * (b ** 2), y * a)

    # dを度数法単位に変換
    d_deg = math.degrees(d)

    print(abs(d_deg))
