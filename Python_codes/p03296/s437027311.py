# coding: utf-8
# submission # - User: herp_sy
# https://atcoder.jp/contests/
#
# lang: Python3 (3.4.3)

import math
import statistics
import numpy as np

n = int(input())
a = list(int(i) for i in input().split())

cnt = 0
b = np.arange(n) + 20000
for i in range(1,n):
  if a[i - 1] == a[i]:
    a[i] = b[i]
    cnt += 1
print(cnt)
