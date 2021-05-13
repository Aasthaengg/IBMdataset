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
s=i()
for i in range(math.ceil(len(s)/2)):
  if not (s[2*i]=="R" or s[2*i]=="U" or s[2*i]=="D"):
    print("No")
    sys.exit()
for j in range(len(s)//2):
  if not (s[2*j+1]=="L" or s[2*j+1]=="U" or s[2*j+1]=="D"):
    print("No")
    sys.exit()
print('Yes')