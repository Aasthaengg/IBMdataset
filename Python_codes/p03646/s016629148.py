def examD():
    K = I()
    N = 50
    A = [i for i in range(N)]
    for i in range(N):
        A[-1-i] +=((K-i+49)//N)
    print(N); print(" ".join(map(str,A)))

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

examD()