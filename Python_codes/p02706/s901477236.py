#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    s = sum(A)
    if s > N:
        print(-1)
    else:
        print(N-s)

main()
