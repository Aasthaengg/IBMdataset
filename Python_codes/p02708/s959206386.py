#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N,K = map(int, input().split())
    MOD = 10**9+7

    count = 0
    for k in range(K,N+2):
        count += ((2*N-k+1)*k//2 - (k-1)*k//2 + 1)%MOD
    print(count%MOD)
main()
