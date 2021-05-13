from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
d = defaultdict(int)
for _ in range(n):
    s = input() 
    d[s[0]] += 1
res = 0
li = ['M','A','R','C','H']
for i in range(3):
    a = li[i]
    for j in range(i+1,4):
        b = li[j]
        for k in range(j+1,5):
            c = li[k]
            res += d[a] * d[b] * d[c]
print(res)