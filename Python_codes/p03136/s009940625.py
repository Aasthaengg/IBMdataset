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
n=int(input())
l=list(map(int,input().split()))
m=max(l)
if 2*m<sum(l):
  print("Yes")
else:
  print("No")