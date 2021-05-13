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

k,x=mp()
m=max(-1000000,x-(k-1))
M=min(1000000,x+k-1)
print(*[i for i in range(m,M+1)])