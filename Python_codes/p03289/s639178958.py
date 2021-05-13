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

S = input()

cond1 = S[0] == 'A'
cond2 = S[2:-1].count('C') == 1
cond3 = True
for i, s in enu(S):
    if i==0:
        continue
    if 2<=i<=len(S)-2 and s=='C':
        continue
    if s == s.upper():
        cond3 = False

if cond1 and cond2 and cond3:
    print('AC')
else:
    print('WA')

