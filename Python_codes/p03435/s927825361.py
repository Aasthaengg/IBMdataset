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

C = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        lu = C[i][j]
        for ii in range(3):
            if i == ii:
                continue
            for jj in range(3):
                if j == jj:
                    continue
                rd = C[ii][jj]
                ld = C[ii][j]
                ru = C[i][jj]

                if lu + rd != ld + ru:
                    print('No')
                    exit()
print('Yes')
