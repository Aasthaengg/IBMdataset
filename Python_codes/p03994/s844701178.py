from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

s = list(input())
k = inp()
n = len(s)
nxa = ord('z') + 1

for i,x in enumerate(s):
    if x == 'a':
        continue
    rem = nxa - ord(x)
    if rem <= k:
        s[i] = 'a'
        k -= rem
if k > 0:
    s[-1] = chr(ord('a') + (ord(s[-1])-ord('a')+k)%26)
print(''.join(s))