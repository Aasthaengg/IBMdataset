"""from collections import *
from itertools import
from bisect import *
from heapq import *

import math
from fractions import gcd
import sys
#input = sys.stdin.readline


"""
import copy
from collections import *
from heapq import *
N=int(input())

lst=[]

if N%2==0:
    for i in range(N-1):
        for m in range(i+1,N):
            if m !=(N-i-1):
                lst.append([i,m])
else:
    for i in range(N):
        for m in range(i+1,N):
            if m !=(N-i-2):
                lst.append([i,m])
print(len(lst))
for a,b in lst:
    print(a+1,b+1)
