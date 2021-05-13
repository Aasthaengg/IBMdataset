import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd
input=sys.stdin.readline
w=0
ah=an=0
N=int(input())
for h in range(1,3501):
    for n in range(h,3501):
        if (4*h*n-N*n-N*h)!=0 and N*n*h%(4*h*n-N*n-N*h)==0:
            w=N*n*h//(4*h*n-N*n-N*h)
            ah=h
            an=n
            break
print(ah,an,w)