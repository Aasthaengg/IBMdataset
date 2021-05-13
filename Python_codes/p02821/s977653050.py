import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from bisect import bisect_left

n,m = map(int,readline().split())
a = list(map(int,readline().split()))

b = [0]*(n+1)
a.sort()
for i in range(n):
  b[i+1] = b[i]+a[i]

def is_ok(arg):
    c = 0
    f = False
    for i in a:
      if c >= m:
        break
      c += (n-bisect_left(a,arg-i))
    if c >= m:
      f = True
    return f

def bisect_ok(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

x = bisect_ok(2*a[-1]+1,1)
ans = 0
cnt = 0
for i in a:
  ind = n-bisect_left(a,x-i)
  cnt += ind
  ans += i*ind+(b[-1]-b[n-ind])
if cnt > m:
  ans -= x*(cnt-m)
print(ans)