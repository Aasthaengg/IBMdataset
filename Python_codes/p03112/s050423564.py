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

a,b,q=map(int,input().split())
s=[int(input()) for _ in range(a)]
t=[int(input()) for _ in range(b)]
x=[int(input()) for _ in range(q)] 

for start in x:
    res=[]
    start_s=bisect.bisect_left(s,start)
    start_t=bisect.bisect_left(t,start)
    if start_s<a and start_t<b:
        res.append(max(s[start_s]-start,t[start_t]-start))
    if start_s-1>-1 and start_t-1>-1:
        res.append(max(start-s[start_s-1],start-t[start_t-1]))
    if start_s<a and start_t-1>-1:
        res.append(2*(s[start_s]-start)+start-t[start_t-1])
        res.append(2*(start-t[start_t-1])+s[start_s]-start)
    if start_t<b and start_s-1>-1:
        res.append(2*(t[start_t]-start)+start-s[start_s-1])
        res.append(2*(start-s[start_s-1])+t[start_t]-start)
    print(min(res))