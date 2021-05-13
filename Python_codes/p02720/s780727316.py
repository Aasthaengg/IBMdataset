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
q=deque(list(range(1,10)))
c=0
while c<a:
  t=q.popleft()
  c+=1
  if t%10!=0:
    q.append(10*t+(t%10)-1)
  q.append(10*t+(t%10))
  if t%10!=9:
    q.append(10*t+(t%10)+1)
print(t)