# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = float('inf')

# 約数列挙
def divisorList(a):
    l = 0
    for i in range(1, int(a**0.5)+1):
        if a % i == 0:
            l += 1
            ii = a / i
            if i != ii:
                l += 1
    return l


N = int(input())    # 数字
res = 0
for i in range(1, N+1):
    if i % 2 == 1:
        if divisorList(i) == 8:
            res += 1

print("{}".format(res))
