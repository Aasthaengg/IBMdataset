import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial
from bisect import bisect_left #bisect_left(list, value)
#from fractions import gcd
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))

A, B = map(int, input().split())

if A<=8 and B<=8:
    print('Yay!')
else:
    print(':(')


