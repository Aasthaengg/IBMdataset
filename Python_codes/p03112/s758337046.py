import sys
 
read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines
inf = float("INF")
a,b,q = map(int, input().split())
s = [None] * (a + 3)
s[0:2] = [-inf,-inf]
s[-1] = inf
t = [None] * (b + 3)
t[0:2] = [-inf,-inf]
t[-1] = inf
for i in range(a):
	s[i+2] = int(input())
for i in range(b):
	t[i+2] = int(input())

from bisect import bisect_left

dp0 = [None] * (a+3)
dp1 = [None] * (b+3)

def f(s,t,x,ss,i):
  if i == 0 and dp0[ss] != None: return abs(x - s[ss]) + dp0[ss]
  elif i == 1 and dp1[ss] != None: return abs(x - s[ss]) + dp1[ss]
  tr = bisect_left(t, s[ss])
  tl = tr - 1
  if i == 0: dp0[ss] = min(abs(s[ss] - t[tl]), abs(s[ss] - t[tr]))
  if i == 1: dp1[ss] = min(abs(s[ss] - t[tl]), abs(s[ss] - t[tr]))
  return abs(x - s[ss]) + min(abs(s[ss] - t[tl]), abs(s[ss] - t[tr]))


for _ in range(q):
  ans = inf
  x = int(input())
  sr = bisect_left(s, x)
  ans = min(ans, f(s,t,x,sr,0))
  ans = min(ans, f(s,t,x,sr - 1,0))
  tr = bisect_left(t, x)
  ans = min(ans, f(t,s,x,tr,1))
  ans = min(ans, f(t,s,x,tr - 1,1))
  print(ans)
  
