import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    K = int(input())
    S = input()
    
    if len(S) <= K:
        print(S)
        return
    
    print(S[0:K]+'...')

main()
