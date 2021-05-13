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

N = int(input())
D, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

et = 0
for a in A:
    et += (D-1)//a[0] + 1
print(et+X)
