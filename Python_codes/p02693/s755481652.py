#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    K = int(input())
    A,B = map(int, input().split())
    if A%K == 0 or A%K + (B-A) >= K:
        print('OK')
    else:
        print('NG')    

main()
