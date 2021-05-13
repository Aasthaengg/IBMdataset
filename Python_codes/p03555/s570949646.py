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
c1=input()
c2=input()
for i in range(3):
  if c1[2-i]!=c2[i]:
    print("NO")
    break
else:
  print("YES")