import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

#input=sys.stdin.readline

s=list(map(int,input()))
n=len(s)
n0=n1=0
for i in range(n):
    if s[i]==1:
        n1+=1
    else:
        n0+=1
print(n-max(n0,n1)+min(n0,n1))