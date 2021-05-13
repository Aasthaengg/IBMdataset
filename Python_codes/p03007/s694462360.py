N = int(input())
A = list(map(int, input().split()))

A.sort()
from collections import deque
d = deque(A)
ans = []
r = d.pop()
for i in range(N-1):
  l = d.popleft()
  if i < N-2:
    nex = d.pop()
  else:
    nex = -1
  if nex>=0:
    ans.append((min(l,r),max(l,r)))
    d.appendleft((-1)*abs(l-r))
  else:
    ans.append((max(l,r),min(l,r)))
    d.appendleft(abs(l-r))
  r = nex
print(d.pop())
for a in ans:
  print(*a,sep=' ')