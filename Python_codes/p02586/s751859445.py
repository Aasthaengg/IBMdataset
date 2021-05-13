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
import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
from numba import jit

@jit
def run_dp(MAP, dp, R, C):
    for i in range(1, R+1):
        for j in range(1, C+1):
            for k in range(4):
                dp[i,j,0] = max(dp[i,j,0], dp[i-1,j,k])
                if MAP[i,j]:
                    dp[i,j,1] = max(dp[i,j,1], dp[i-1,j,k]+MAP[i,j])

                dp[i,j,k] = max(dp[i,j,k], dp[i,j-1,k])
                if MAP[i][j] and k < 3:
                    dp[i,j,k+1] = max(dp[i,j,k+1], dp[i,j-1,k] + MAP[i,j])
    return dp[R, C].max()

def run():
    R,C,K = map(int, sysread().split())
    MAP = np.zeros((R + 1, C + 1), dtype=np.int64)
    for i in range(K):
        r, c, v = map(int, sysread().split())
        MAP[r, c] = v

    dp = np.zeros((R+1, C+1, 4), dtype= np.int64)

    run_dp(MAP, dp, R, C)

    #print(dp)
    #for m in MAP:
    #   print(m)
    ans= run_dp(MAP, dp, R, C)

    print(ans)

if __name__ == "__main__":
    run()