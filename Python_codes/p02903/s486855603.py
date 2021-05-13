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
h,w,a,b=map(int,input().split())
ans=[[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if (i<b and j<a) or (i>=b and j>=a):
            ans[i][j]=1
for i in range(h):
	L=[str(x) for x in ans[i]]
	L="".join(L)
	print(L)