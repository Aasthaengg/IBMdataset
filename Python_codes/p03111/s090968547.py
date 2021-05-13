#import sys
#import numpy as np
#import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect

n,A,B,C=map(int,input().split())
l=[int(input()) for _ in range(n)]
inf=10**9
def rec(i,a,b,c):
    if i==n:
        if not a or not b or not c:
            return inf
        return abs(A-a)+abs(B-b)+abs(C-c)
    res=rec(i+1,a,b,c)
    res=min(res,rec(i+1,a+l[i],b,c)+(10 if a else 0))
    res=min(res,rec(i+1,a,b+l[i],c)+(10 if b else 0))
    res=min(res,rec(i+1,a,b,c+l[i])+(10 if c else 0))

    return res
print(rec(0,0,0,0))