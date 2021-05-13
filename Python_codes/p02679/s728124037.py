# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.readline
read = sys.stdin.read
from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product#accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
def run():
    mod = 1000000007
    N, *AB = map(int, read().split())
    A_B = []
    INF = float('inf')
    zerozero = 0
    for i in range(N):
        a = AB[2*i]
        b = AB[2*i+1]
        if a== 0 and b == 0:
            zerozero += 1
        elif b == 0:
            A_B.append((INF, 0))
        elif a == 0:
            A_B.append((0, INF))
        else:
            tmp = math.gcd(a,b)
            if a / b > 0 :v = 1
            else: v = -1
            A_B.append((abs(a//tmp), v * abs(b//tmp)))

    comb_dict = defaultdict(lambda:[0,0])

    for ai, bi in A_B:
        if ai == INF:
            comb_dict[0][1] += 1
        elif bi == INF:
            comb_dict[0][0] += 1
        elif bi < 0:
            comb_dict[(ai,bi)][0] += 1
        else:
            comb_dict[(bi, -ai)][1] += 1

    ret = 1
    for _, val_list in comb_dict.items():
        a,b = val_list
        if a == 0 or b == 0:
            ret *= pow(2, max(a,b), mod)
        else:
            ret *= pow(2, a, mod) + pow(2, b, mod) - 1
        ret %= mod
    ret += zerozero-1
    print(ret%mod)



if __name__ == "__main__":
    run()