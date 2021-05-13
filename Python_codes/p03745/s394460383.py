#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
n = int(input())
#  = map(int, input().split())
a  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

if n == 1:
    print(1)
else:
    ans = 1
    state = lambda n1, n2: 0 if n1 == n2 else (1 if n2 > n1 else -1)
    diff = [state(a1, a2) for a1, a2 in zip(a[:-1], a[1:]) if state(a1, a2) != 0]

    p = 1
    while p < len(diff):
        if abs(diff[p] - diff[p-1]) == 2:
            ans += 1
            p += 1

        p += 1

    print(ans)
