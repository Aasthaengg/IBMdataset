# -*- coding: utf-8 -*-
import math

N = int(input())

for x in range(N,0,-1):
    val = int(x * 1.08)
    if val == N:
        print(x)
        exit()

print(':(')