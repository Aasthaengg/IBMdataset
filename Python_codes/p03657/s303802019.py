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

a,b=mp()
if a%3==0 or b%3==0 or (a+b)%3==0:
    print("Possible")
else:
    print("Impossible")