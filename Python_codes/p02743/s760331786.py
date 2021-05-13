#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))

a, b, c = map(int, input().split())

if a+b < c:
    left = 4*a*b
    right = (c-a-b)**2
    if left < right:
        print('Yes')
    else:
        print('No')
else:
    print('No')

