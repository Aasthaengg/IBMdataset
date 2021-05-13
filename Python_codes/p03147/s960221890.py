#import sys
#import numpy as np
import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n=int(input())
h=list(map(int,input().split()))
m=max(h)
c=0
for i in range(1,m+1):
    if h[0]>=i:
        c+=1
    for j in range(1,n):
        if h[j]>=i and h[j-1]<i:
            c+=1
print(c)