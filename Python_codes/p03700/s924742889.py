from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd
import sys
#input = sys.stdin.readline

import copy

N,A,B=map(int,input().split())
H=[int(input()) for i in range(N)]
H.sort()
ng=0
ok=10**18
A-=B
while ok-ng>1:

    mid=(ok+ng)//2
    c=bisect_right(H,mid*B)

    _sum=0
    for i in range(c,N):
        Z=H[i]-mid*B
        _sum+=Z//A+bool(Z%A)
    #print(_sum)
    if mid>=_sum:
        ok=mid
    else:
        ng=mid
print(ok)
