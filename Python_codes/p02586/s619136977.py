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
import bisect
import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal


from numba import jit

@jit
def run_dp(MAP, dp, Rs, Cs):
    for i in range(1, len(Rs)+1):
        for j in range(1, len(Cs)+1):
            for k in range(4):
                dp[i,j,0] = max(dp[i,j,0], dp[i-1,j,k])
                if MAP[i,j]:
                    dp[i,j,1] = max(dp[i,j,1], dp[i-1,j,k]+MAP[i,j])

                dp[i,j,k] = max(dp[i,j,k], dp[i,j-1,k])
                if MAP[i][j] and k < 3:
                    dp[i,j,k+1] = max(dp[i,j,k+1], dp[i,j-1,k] + MAP[i,j])
    return dp[len(Rs), len(Cs)].max()

def run():
    R,C,K = map(int, sysread().split())
    Rs = set()
    Cs = set()
    vals = []
    for i in range(K):
        r, c, v = map(int, sysread().split())
        vals.append((r, c, v))
        Rs.add(r)
        Cs.add(c)
    #Rs = sorted(list(Rs))
    Rs = np.array(sorted(list(Rs)))
    #Cs = sorted(list(Cs))
    Cs = np.array(sorted(list(Cs)))
    r_idx = {r:i+1 for i, r in enumerate(Rs)}
    c_idx = {c:i+1 for i, c in enumerate(Cs)}
    #MAP = [[0] * (len(Cs)+1) for _ in range(len(Rs)+1)]
    MAP = np.zeros((len(Rs)+1, len(Cs)+1), dtype= np.int64)
    for r,c,v in vals:
        rn = r_idx[r]
        cn = c_idx[c]
        MAP[rn][cn] = v

    #dp = [[[0] * 4 for _ in range(len(Cs)+1)] for i in range(len(Rs)+1)]
    dp = np.zeros((len(Rs)+1, len(Cs)+1, 4), dtype= np.int64)

    run_dp(MAP, dp, Rs, Cs)

    #print(dp)
    #for m in MAP:
    #   print(m)
    ans= run_dp(MAP, dp, Rs, Cs)

    print(ans)

if __name__ == "__main__":
    run()