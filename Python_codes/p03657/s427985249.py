def examA():
    A, B = LI()
    if A%3==0 or B%3==0 or (A+B)%3==0:
        ans = "Possible"
    else:
        ans = "Impossible"
    print(ans)



import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examA()
