#import sys
#import numpy as np
import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n=int(input())
node=[]
if n%2==0:
    for i in range(n):
        for j in range(i,n):
            if j==i or j==n-1-i:
                continue
            node.append((i+1,j+1))
else:
    for i in range(n):
        for j in range(i,n):
            if j==i or j==n-2-i:
                continue
            node.append((i+1,j+1))
    
print(len(node))
for i in node:
    print(*i) 