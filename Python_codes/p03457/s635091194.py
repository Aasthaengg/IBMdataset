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

N = int(input())
txy = [list(map(int, input().split())) for _ in range(N)]

for txyi, txyip in zip([[0, 0, 0]] + txy[:-1], txy):
    ti, xi, yi = txyi
    tip, xip, yip = txyip
    dift = tip - ti
    difd = abs(xip-xi) + abs(yip-yi)
    if difd%2 != dift%2:
        print('No')
        exit()
    if dift < difd:
        print('No')
        exit()
print('Yes')

