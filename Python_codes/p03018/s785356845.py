from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

s = input()
n = len(s)
res = 0
bc = 0
i = n-1
while i >= 0:
    if s[i] == 'A':
        res += bc
        i -= 1
    elif i != 0 and s[i-1] == 'B' and s[i] == 'C':
        bc += 1
        i -= 2
    else:
        bc = 0
        i -= 1
print(res)