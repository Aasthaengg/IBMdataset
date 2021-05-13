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
n=int(input())
ans=0
for i in range(n):
    x,u=input().split()
    if u=="BTC":
        x=float(x)
        ans+=380000*x
    else:
        x=int(x)
        ans+=x
print(ans)