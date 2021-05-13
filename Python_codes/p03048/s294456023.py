#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
#  = int(input())
r, g, b, n  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

ans = 0
for r_ in range(n+1):
    for g_ in range(n+1):
        sum_ = n - (r_ * r + g_ * g)
        if sum_ >= 0 and sum_ % b == 0:
            ans += 1

print(ans)


