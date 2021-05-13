# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
N, X, T = map(int, input().split())

times = N//X
remain = N%X
if remain:
  times += 1
print(times * T)

