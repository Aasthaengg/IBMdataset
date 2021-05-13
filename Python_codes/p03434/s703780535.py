# coding: utf-8
import math
n = input()
N = map(int, input().split())
N = sorted(list(N), reverse=True)

a = sum(N[::2])
b = sum(N[1::2])
print(a - b)
