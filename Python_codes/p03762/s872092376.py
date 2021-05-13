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

n,m = inm()
x = inl()
y = inl()
ax = 0
k = -n+1
for i in range(n):
    ax = (ax+k*x[i])%R
    k += 2
ay = 0
k = -m+1
for i in range(m):
    ay = (ay+k*y[i])%R
    k += 2
print((ax*ay)%R)
