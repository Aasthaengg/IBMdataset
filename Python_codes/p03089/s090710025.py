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
b=list(map(int,input().split()))
ans=[]
while True:
    f=False
    for i in range(len(b)-1,-1,-1):
        if b[i]!=i+1:
            continue
        else:
            ans.append(b[i])
            b.pop(i)
            f=True
            break
    if not b:
        break
    if not f:
        print(-1)
        exit()
for i in range(n):
    print(ans[n-1-i])