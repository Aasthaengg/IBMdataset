#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')
A,B,X=map(int, input().split())
if A > X:
    print('NO')
elif X-A <= B:
    print('YES')
else:
    print('NO')
