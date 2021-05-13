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

a,b=mp()
if b==1:
    print(0)
    exit()
for i in range(1,100):
    if 1+(a-1)*i>=b:
        print(i)
        exit()