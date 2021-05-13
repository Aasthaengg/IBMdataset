import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions  import gcd
#input=sys.stdin.readline
#import bisect

n=int(input())
c=0
for i in range(n):
    a=int(input())
    if a%2==0:
        c+=1

if c==n:
    print("second")
else:
    print("first")