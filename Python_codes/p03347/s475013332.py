# -*- coding: utf-8 -*-
# 
import math
import sys
import itertools
import numpy as np

n =int(input())
x = [int(input()) for i in range(n)] 
sousa=0
if x[0] != 0:
    print("-1")
    exit()
for i in range(1,n):
    if x[i] > x[i-1] + 1:
        print("-1")
        exit()
    elif x[i] == x[i-1] + 1:
        sousa += 1
    else:
        sousa += x[i]
print(sousa)

