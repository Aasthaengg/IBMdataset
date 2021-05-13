import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

h=int(input())
w=int(input())
n=int(input())
a=max(h,w)
print((n-1)//a+1)