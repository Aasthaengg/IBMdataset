import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

n,m,k=map(int,input().split())
f=False
for i in range(n+1):
    for j in range(m+1):
        if m*i+n*j-2*i*j==k:
            print("Yes")
            f=True
            break
    if f:
        break
else:
    print("No")