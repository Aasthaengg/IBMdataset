import sys
input = sys.stdin.readline
n = int(input())
a = [int(i) for i in input().split()]
from collections import deque
l = []
r = []
for i in a:
  if i < 0:
    l.append(i)
  else:
    r.append(i)
    
ll = len(l)
rr = len(r)
r.sort()
l.sort()
ans = []
l = deque(l)
r = deque(r)

for i in range(n-1):
  if ll == 0:
    mi = r.popleft()
    ma = r.pop()
    ans.append((mi,ma))
    l.append(mi-ma)
    ll += 1
  else:
    if rr > 1:
      L = l.pop()
      R = r.pop()
      ans.append((L,R))
      l.append(L-R)
      rr -= 1
    elif rr == 1:
      L = l.pop()
      R = r.pop()
      ans.append((R,L))
      r.append(R-L)
    else:
      mi = l.popleft()
      ma = l.pop()
      ans.append((ma,mi))
      r.append(ma-mi)
      rr += 1
      
p,q = ans[-1]
print(abs(p-q))
if p < q:
  ans[-1] = (q,p)
for i,j in ans:
  print(i,j)