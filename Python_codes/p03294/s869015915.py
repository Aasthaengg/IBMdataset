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

ans = 0
for a_ in a:
    ans += a_ -1

print(ans)

