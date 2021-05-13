#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

import bisect
n = inn()
a = inl()
a.sort()
a.append(10**9+1)
b = inl()
b.sort()
b.append(10**9+1)
c = inl()
c.sort()
c.append(10**9+1)
sm = 0
for i in range(n):
    p = bisect.bisect_left(a,b[i])
    q = bisect.bisect_right(c,b[i])
    sm += p*(n-q)
print(sm)
