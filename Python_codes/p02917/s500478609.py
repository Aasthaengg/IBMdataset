mod=10**9+7
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
a=ii()
l=list(mi())
ans=l[0]
for i in range(a-2):
  ans+=min(l[i],l[i+1])
print(ans+l[-1])