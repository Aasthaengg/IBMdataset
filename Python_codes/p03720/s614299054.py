#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
n, m  = map(int, input().split())
#  = list(map(int, input().split()))
ab = [tuple(map(int, input().split())) for i in range(m)]
#
# c = collections.Counter()

doro = [0] * (n + 1)

for ab_ in ab:
    a, b = ab_
    doro[a] += 1
    doro[b] += 1

for d in doro[1:]:
    print(d)
