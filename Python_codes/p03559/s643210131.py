from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
A = sorted(inpl())
B = sorted(inpl())
C = sorted(inpl())
cnt = [0] * n
res = 0
for i,b in enumerate(B):
    c = bisect.bisect_left(C,b+1)
    cnt[i] = n-c

acc = [0]
for x in cnt:
    acc += [acc[-1] + x]
su = sum(cnt) 
for i,a in enumerate(A):
    c = bisect.bisect_left(B,a+1)
    res += su - acc[c]
print(res)