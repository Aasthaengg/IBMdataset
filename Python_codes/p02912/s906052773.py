import math
import sys
from collections import deque
import heapq
import copy
import itertools
from itertools import permutations
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()
a,b=mi()
l=list(mi())
l=list(map(lambda x: x*-1 , l))
heapq.heapify(l)
for i in range(b):
  s=heapq.heappop(l)
  s=(-1)*(((-1)*s)//2)
  heapq.heappush(l,s)
ans=0
for i in range(a):
  d=heapq.heappop(l)
  ans+=(-1)*d
print(ans)