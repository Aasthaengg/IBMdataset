#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = input()
x  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

sum_ = 0
for i in range(x+1):
    sum_ += i

    if sum_ >= x:
        print(i)
        break
