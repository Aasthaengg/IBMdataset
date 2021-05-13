#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
n = int(input())
s = input()
t = input()
#  = map(int, input().split())
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

for i in range(n-1, -1, -1):
    # print(s[-(i+1):], t[:i+1])
    if s[-(i+1):] == t[:i+1]:
        l = len(t[:i+1])
        print((len(t) - l) * 2 + l)
        break
else:
    print(len(s) * 2)
