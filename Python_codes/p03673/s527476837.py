import sys
from collections import deque
finput=lambda: sys.stdin.readline().strip()

n=int(finput())
a=finput().split()
b=deque()

for i in range(n):
  if (n-i)%2==0:
    b.append(a[i])
  else:
    b.appendleft(a[i])
print(' '.join(b))