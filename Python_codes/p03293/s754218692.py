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
T = input()

for dif in range(len(S)):
    ok = True
    for i, t in zip(range(dif, dif+len(S)), T):
        ri = i%len(S)
        if S[ri] != t:
            ok = False
        if not(ok):
            break
    else:
        if ok:
            print('Yes')
            exit()
else:
    print('No')