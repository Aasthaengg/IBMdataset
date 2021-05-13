#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    A = list(map(int, input().split()))

    C = [0]*N
    for a in A:
        C[a-1] += 1

    for c in C:
        print(c)

main()
