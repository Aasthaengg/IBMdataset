# -*- coding: utf-8 -*-
# 整数の入力
a, b, c = map(int, input().split())
result = 0
if a + b + 1 >= c:
  result = b + c
else:
  result = b + (a + b + 1)
# 出力
print("{}" .format(result))