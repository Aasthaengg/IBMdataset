#import numpy as np
#import math
#from decimal import *
#from numba import njit
from math import floor

#@njit
def main():
    A,B,N = map(int, input().split())
    
    def f(x):
        return floor(A*x/B)-A*floor(x/B)

    print(f(min(N, B-1)))
main()
