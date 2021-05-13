#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left, bisect_right #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep='\n')

S = input()
K = int(input())

for i, s in enu(S):
    if s != '1':
        print(s)
        exit()
    if i == K-1:
        print(s)
        exit()
