from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

a,b,c,d = inpl()
x = c-a
y = d-b
res = ''
res += 'U' * y + 'R' * x
res += 'D' * y + 'L' * x
res += 'L' + 'U' * (y+1) + 'R' * (x+1) + 'D'
res += 'R' + 'D' * (y+1) + 'L' * (x+1) + 'U'
print(res)
