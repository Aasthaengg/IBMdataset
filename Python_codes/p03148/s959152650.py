import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from operator import itemgetter
from collections import defaultdict,deque

n,k = map(int,readline().split())
chk = []
for i in range(n):
  t,d = map(int,readline().split())
  chk.append((t,d))
chk = sorted(chk,key=itemgetter(1),reverse=True)

T = defaultdict(int)
d = deque()
s = set()
ans = []
aa = 0
for i in range(k):
  p,q = chk[i]
  T[p] += 1
  if T[p] > 1:
    d.append(q)
  s.add(p)
  aa += q
  
l = len(s)
aa += l**2
if k == n or l == k:
  print(aa)
  exit()
  
ans = aa
cnt = k-l
for p,q in chk[k:]:
  if T[p] == 0:
    T[p] += 1
    P = d.pop()
    aa -= P
    aa += q+2*l+1
    l += 1
    cnt -= 1
    ans = max(ans,aa)
  if cnt == 0:
    break
    
print(ans)