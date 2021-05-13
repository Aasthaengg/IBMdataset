#import numpy as np
#import math
#from decimal import *
#from numba import njit
import re

#@njit
def main():
    S = input()
    T = input()

    if re.match(r'^[a-z]*$', S) and\
        re.match(r'^[a-z]*$', T) and\
        1 <=len(S) and\
        len(S) <= 10 and\
        len(T) == len(S) + 1 and\
        T[0:len(T)-1] == S:
        print('Yes')
    else:
        print('No')
    

main()
