#import sys
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

k,t=map(int,input().split())
a=list(map(int,input().split()))
x=max(a)
if k-x>=x-1:
    print(0)
else:
    print(2*x-1-k)