#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np
 
#  = int(input())
n, a, b, c, d  = map(int, input().split())
a -= 1
b -= 1
c -= 1
d -= 1
s  = input()
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()

is_rock2 = '##' in s[a:d+1]
is_empty3 = '...' in s[b-1:d+2]

joken = (not is_rock2) and (is_empty3 if c > d else 1)
print('Yes' if joken else 'No')
