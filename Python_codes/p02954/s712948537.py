# coding: utf-8
import sys
# from operator import itemgetter
sysread = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)
from heapq import heappop, heappush
#from collections import OrderedDict, defaultdict
#import math
#from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque
#import numba

def run():
    S = input()
    N = len(S)
    group = [[]]
    g = []
    l = []
    init = 0
    indice = 0
    group_num = 0
    ind = [-1] * N
    for k in range(N):
        if S[k] == 'R':
            group[group_num].append(k)
            ind[k] = indice
            indice +=1
            g.append(group_num)
            continue
        else:
            if not init:
                l.append(indice-1)
                init = 1
            if k < N-1 and S[k+1] == 'R':
                group[group_num].append(k)
                g.append(group_num)
                group_num += 1
                group.append([])
                init = 0
                ind[k] = indice
                indice=0
            else:
                group[group_num].append(k)
                g.append(group_num)
                ind[k] = indice
                indice+=1

    #print(group)
    #print(ind)
    #print(l)
    #print(g)
    #print('')
    ret = [0] * N
    for i in range(N):
        _l = l[g[i]]
        indice = ind[i]
        if indice <= _l:
            tmp = group[g[i]][_l + (_l - indice) % 2]
            ret[tmp]+=1
        if indice >= _l+1:
            tmp = group[g[i]][_l + (_l - indice) % 2]
            ret[tmp] += 1
        #print(ret)

    print(' '.join([str(s) for s in ret]))

if __name__ == "__main__":
    run()