# -*- coding: utf-8 -*-
# 整数の入力
n = int(input())

power = 1
for i in range(1, n+1):
    power *= i
    if i % 10 == 0:
        power %= (10 ** 9 + 7)

ret = power % (10 ** 9 + 7)
# 出力
print(ret)
