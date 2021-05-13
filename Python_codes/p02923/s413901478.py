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
c=0
ans=0
if a==1:
  print(0)
else:
  for i in range(1,a):
    if l[i]<=l[i-1]:
      c+=1
    else:
      if ans<c:
        ans=c
      c=0
  print(max(ans,c))