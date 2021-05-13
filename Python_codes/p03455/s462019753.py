# -*- coding: utf-8 -*-
# 整数の入力
a, b = map(int, input().split())
if a * b % 2 == 0:
  x = "Even"
else:
  x = "Odd"
print(x)