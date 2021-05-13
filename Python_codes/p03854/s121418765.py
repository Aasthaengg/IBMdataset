#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

s=SI()
s=s[::-1]
i=0
while i<len(s):
    if s[i:i+5]=="maerd" or s[i:i+5]=="esare":
        i+=5
    elif s[i:i+6]=="resare":
        i+=6
    elif s[i:i+7]=="remaerd":
        i+=7
    else:
        print("NO")
        sys.exit()
print("YES")


