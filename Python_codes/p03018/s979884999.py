# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7


def run():
    S = input()
    SS = []
    dic = {'A': -1, 'B' : -2, 'C' : -3}
    chain = False
    skip = False
    for i in range(len(S)):
        if not chain:
            if S[i:i+2] == 'BC':
                chain = True
                skip = True
                SS.append(1)
            else:
                SS.append(dic[S[i]])
        else:
            if skip:
                skip = False
                continue
            else:
                if S[i:i+2] == 'BC':
                    skip = True
                    SS[-1] += 1
                else:
                    SS.append(dic[S[i]])
                    chain = skip = False
    #print(SS)
    ans = 0
    BCbox = 0
    for x in SS[::-1]:
        if x > 0:
            BCbox += x
        elif x == -1:
            ans += BCbox
        else:
            BCbox = 0
    print(ans)



if __name__ == "__main__":
    run()
