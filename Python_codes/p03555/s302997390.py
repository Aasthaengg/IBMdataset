import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
import itertools
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

c=[input() for i in range(2)]
ans="YES"
if c[0][0]!=c[1][2]:
    ans="NO"
if c[0][1]!=c[1][1]:
    ans="NO"
if c[0][2]!=c[1][0]:
    ans="NO"
print(ans)