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
pri = lambda x: print(*x, sep='\n')

a, b, c, d = map(int, input().split())

direct = abs(a-c) <= d

chk1 = abs(a-b)<=d
chk2 = abs(b-c)<=d
indirect = chk1 and chk2

if direct or indirect:
    print('Yes')
else:
    print('No')
