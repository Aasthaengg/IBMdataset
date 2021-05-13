import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

input=sys.stdin.readline
x=[int(input()) for _ in range(5)]
k=int(input())

if x[-1]-x[0]<=k:
  print("Yay!")
else:
  print(":(")