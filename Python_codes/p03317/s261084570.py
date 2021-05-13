#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n,k=map(int,input().split())
a=list(map(int,input().split()))
ix=a.index(1)
i=math.ceil((n-k)/(k-1))+1
print(i)