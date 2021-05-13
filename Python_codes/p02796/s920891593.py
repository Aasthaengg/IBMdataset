import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
#from collections import deque
#import heapq
#from fractions  import gcd
input=sys.stdin.readline
n=int(input())
xl=[list(map(int,input().split())) for _ in range(n)]
xl.sort(key=lambda x:x[0])
xb=xl[0][0]
lb=xl[0][1]
c=0
for i in range(1,n):
    x=xl[i][0]
    l=xl[i][1]
    if x-l<xb+lb:
        c+=1
        if x+l<xb+lb:
            xb=x
            lb=l
    else:
        xb=x
        lb=l
print(n-c)