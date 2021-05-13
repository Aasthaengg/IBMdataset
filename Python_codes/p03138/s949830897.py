from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,k = inpl()
a = inpl()
a.sort()
ln = len(bin(max(k,a[-1]))) - 2 #2進数に直した時の桁数
bit = [0 for i in range(ln)]
res = 0
ans = 0
for x in a:
    for i in range(ln):
        if i: 
            (x>>1) % 2
            x = x>>1
        if x%2:
            bit[i] += 1
    # print(bit)
for i,j in enumerate(bit):
    if j < n/2:
        bit[i] = 1
    else:
        bit[i] = 0
# print(bit)
for i in range(ln):
    if bit[ln-i-1]:
        c = pow(2,ln-i-1)
        if k >= c:
            res += c
            k -= c

for i in a:
    ans += i^res
print(ans)
