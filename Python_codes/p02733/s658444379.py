# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque
def run():
    H,W,K = map(int, sysread().split())
    S = []
    for i in range(H):
        S.append(list(accumulate(list(map(int, list(input()))))))
    for h in range(1, H):
        for w in range(W):
            S[h][w] += S[h-1][w]

    ret = float('inf')

    for idxes_ in product((0,1), repeat=H-1):
        l = 0
        r = 1
        idxes = [0]
        for i, val in enumerate(idxes_, 1):
            if val == 1:
                idxes.append(i)
        idxes.append(H)
        min_cut = len(idxes) - 2
        while r <= W:
            for i in range(len(idxes)-1):
                if idxes[i] == 0 and l == 0:
                    cri = S[idxes[i+1]-1][r-1]
                elif l == 0:
                    cri = S[idxes[i+1]-1][r-1] - S[idxes[i]-1][r-1]
                elif idxes[i] == 0:
                    cri = S[idxes[i+1]-1][r-1] - S[idxes[i+1]-1][l-1]
                else:
                    cri = S[idxes[i+1]-1][r-1] - S[idxes[i]-1][r-1] - S[idxes[i+1]-1][l-1] + S[idxes[i]-1][l-1]

                if cri > K:
                    r -= 1
                    if l == r:
                        min_cut = float('inf')
                        r = W+1
                        break
                    l = r
                    min_cut += 1
                    break
            r += 1
        ret = min(ret, min_cut)

    print(ret)




if __name__ == "__main__":
    run()
