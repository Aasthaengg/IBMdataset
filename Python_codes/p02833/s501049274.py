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
n=int(input())
a=5
ans=0
if n%2==1:
  print(0)
  exit()
while True:
    if a>n:
        break
    ans+=(n//a)//2
    a*=5
print(ans)