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

a=i()
b=i()
c=0
for i in range(3):
  if a[i]==b[i]:
    c+=1
print(c)