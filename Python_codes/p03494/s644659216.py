# -*- coding: utf-8 -*-
import math

N = int(input()) #使用しない

maxn = 1000000000
for a in input().split():

    count = 0
    b = int(a)
    while( b % 2 == 0):
        b = b // 2
        count += 1

    maxn = min(maxn, count)

print(maxn)