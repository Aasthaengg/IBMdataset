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
pl = lambda x: print(*x, sep='\n')

l = list(map(int, input().split()))
l.sort()

dif = 2*l[2] - l[1] - l[0]
if dif%2==0:
    print(dif//2)
else:
    print((dif+3)//2)
