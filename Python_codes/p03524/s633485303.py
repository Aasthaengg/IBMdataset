#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
s  = input()
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
c = collections.Counter(s)

v = [v_ for v_ in c.values() if v_ != 0]

if len(s) == 1:
    print('YES')
    exit()

if len(s) == 2: 
    print('YES' if len(v) == 2 else 'NO')
    exit()

if len(v) <= 2:
    print('NO')
else:
    print('YES' if max(v) - min(v) <= 1 else 'NO')
