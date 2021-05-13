from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

s = input()
k = inp()
n = len(s)
t = []
for i in s:
    t.append(ord(i) - ord('a'))
se = set()
for i in range(26):
    for j in range(n):
        if t[j] == i:
            for l in range(j,min(j+k,n)):
                tmp = s[j:l+1]
                if tmp == '':
                    continue
                se.add(tmp)
    if len(se) >= k:
        break
res = sorted(list(se))
print(res[k-1])