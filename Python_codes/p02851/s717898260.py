import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k = map(int,readline().split())
if k == 1:
  print(0)
  exit()
  
a = [0]+[int(i) for i in readline().split()]
for i in range(1,n+1):
  a[i] = a[i-1]+a[i]
  
a = [(ai-i)%k for i,ai in enumerate(a)]
#print(a)
from collections import Counter,deque
c = Counter({a[0]:1})
d = deque([a[0]])
ans = 0
cnt = 1
for j,aj in enumerate(a[1:]):
  ans += c[aj]
  d.append(aj)
  c.update({aj:1})
  cnt += 1
  if cnt >= k:
    p = d.popleft()
    c.update({p:-1})
  
print(ans)
