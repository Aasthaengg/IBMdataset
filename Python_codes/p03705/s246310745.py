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
n,a,b=map(int,input().split())
ans=(b*(n-1)+a-a*(n-1)-b)+1
if ans<0:
  print(0)
  exit()
print(ans)