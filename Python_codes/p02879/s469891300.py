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
a=mi()
ans=1
for i in a:
  if 1<=i<=9:
    ans*=i
  else:
    print(-1)
    sys.exit()
print(ans)