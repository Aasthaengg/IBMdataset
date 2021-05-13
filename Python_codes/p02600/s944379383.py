# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = float('inf')

a = int(input())    # 数字

for i in range(8):
    M = 2000 - 200 * i
    m = 1800 - 200 * i
    if m <= a < M:
        print(i + 1)
