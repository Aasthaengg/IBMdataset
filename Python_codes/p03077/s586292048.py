import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

input=sys.stdin.readline
n=int(input())
x=[int(input()) for _ in range(5)]
t=[0]*5
t[0]=math.ceil(n/x[0])
m=x[0]
for i in range(1,5):
    if x[i]>=m:
        t[i]=t[i-1]+1
    else:
        t[i]=i+math.ceil(n/x[i])
        m=x[i]
print(t[-1])