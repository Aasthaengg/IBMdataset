#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
n  = int(input())
#  = map(int, input().split())
a  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

ans_ = 0
for i, a_ in enumerate(a):
    if a[a_-1] == i + 1: 
        ans_ += 1
print(ans_ // 2)
