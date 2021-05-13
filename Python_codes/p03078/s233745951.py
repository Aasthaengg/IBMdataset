import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
x,y,z,k = map(int,readline().split())
a = [int(i) for i in readline().split()]
b = [int(i) for i in readline().split()]
c = [int(i) for i in readline().split()]
from heapq import heappush,heappop,heapify
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

chk = [(-(a[0]+b[0]+c[0]),0,0,0)]
heapify(chk)
C = set((0,0,0))
ans = []
for i in range(k):
  p,q,r,s = heappop(chk)
  ans.append(-p)
  if not (q+1,r,s) in C and q < x-1:
    C.add((q+1,r,s))
    heappush(chk,(-(a[q+1]+b[r]+c[s]),q+1,r,s))
  if not (q,r+1,s) in C and r < y-1:
    C.add((q,r+1,s))
    heappush(chk,(-(a[q]+b[r+1]+c[s]),q,r+1,s))
  if not (q,r,s+1) in C and s < z-1:
    C.add((q,r,s+1))
    heappush(chk,(-(a[q]+b[r]+c[s+1]),q,r,s+1))
    
for i in ans:
  print(i)