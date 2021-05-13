import math
import sys
from collections import deque
import heapq
import copy
import itertools
from itertools import permutations
from itertools import combinations
import bisect
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()
a,b,c=mi()
h=c/(a**2)
if h>b/2:
  print(math.degrees(math.atan(2*(b-h)/a)))
else:
  print(90-math.degrees(math.atan(2*c/(a*b*b))))