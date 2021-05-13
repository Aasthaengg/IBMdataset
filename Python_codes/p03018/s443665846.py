from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

s = input()
n = len(s)
ind = n-1
cnt = 0
res = 0
f = False
while ind >= 0:
    if ind-1 >= 0 and (s[ind-1],s[ind]) == ('B','C'):
        f = True
        cnt += 1
        ind -= 2
    elif f and s[ind] == 'A':
        res += cnt
        ind -= 1
    else:
        f = False
        cnt = 0
        ind -= 1
print(res)
