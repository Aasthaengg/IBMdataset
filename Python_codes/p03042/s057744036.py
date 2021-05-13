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

s=int(input())
a=s//100
b=s%100
if 0<a<13:
    if 0<b<13:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 0<b<13:
        print("YYMM")
    else:
        print("NA")
