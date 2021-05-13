# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = float('inf')

N = int(input())    # 数字
S = input()     # 文字列

res = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            src = i
            num = 0
            for s in S:
                if int(s) == src:
                    if num == 0:
                        src = j
                        num = 1
                    elif num == 1:
                        src = k
                        num = 2
                    elif num == 2:
                        res += 1
                        break

print("{}".format(res))
