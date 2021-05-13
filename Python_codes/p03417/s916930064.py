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

N, M = map(int, input().split())
if N>M:
    N, M = M, N

if N==1 and M==1:
    print(1)
elif N==1 and M!=1:
    print(M-2)
elif N==2:
    print(0)
else:
    v = N*M - 2*M - 2*(N-2)
    print(v)


