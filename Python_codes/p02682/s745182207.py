#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    A,B,C,K = map(int, input().split())
    print(min(A,K)-max(0,min(C, K-A-B)))

main()
