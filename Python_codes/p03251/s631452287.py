#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
from fractions  import gcd
#input=sys.stdin.readline
import bisect
n,m,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x.sort()
y.sort()
i=x[-1]
j=y[0]
if i<j:
    for k in range(i+1,j+1):
        if X<k<=Y:
            print("No War")
            break
    else:
        print("War")
    
else:
    print("War")