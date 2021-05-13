#!/usr/bin/env python3

#import
#import math
#import numpy as np
X = int(input())

li = [i ** 5 for i in range(1005)]

for a in range(1000):
    for b in range(1000):
        t1 = li[a] - li[b]
        t2 = li[a] + li[b] if b % 2 == 1 else t1
        if t1 == X:
            print(a, b)
            exit()
        elif  t2 == X:
            print(a, -b)
            exit()
