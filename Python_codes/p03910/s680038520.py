#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())

i = 0
isum = 0

while isum < N:
    i += 1
    isum += i

t = isum - N

for j in range(1, i + 1):
    if j != t:
        print(j)