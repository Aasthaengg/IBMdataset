import math
import sys
from collections import deque
import copy
import itertools
from itertools import permutations
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()
a,b=mi()
ans=0
while a<=b:
  a*=2
  ans+=1
print(ans)