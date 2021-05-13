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

n = inp()
a = inpl()
l = 0; r = 0
bit = [False] * 22
res = 0
def f(n):
    return "".join(list(bin(n))[2:])
def back(l):
    c = f(a[l])[::-1]
    for i,t in enumerate(c):
        if t == '1':
            bit[i] = False
def check(c):
    for i,t in enumerate(c):
        if t == '1' and bit[i]:
            return False
    return True

def write(c):
    for i,t in enumerate(c):
        if t == '1': bit[i] = True

while l < n and r < n+1:
    if r == n:
        res += r-l
        back(l)
        l += 1
        continue
    now = f(a[r])[::-1]
    if check(now):
        write(now)
        r += 1
    else:
        res += r-l
        back(l)
        l += 1
    # print(l,r,res,bit)
res += r-l
print(res)