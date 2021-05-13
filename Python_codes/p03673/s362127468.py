n=int(input())
a=list(map(int,input().split()))
mode=0
from collections import deque
b=deque([])
for i in range(n):
  if i%2==0:
    b.append(a[i])
    mode+=1
    mode%=2
  else:
    b.appendleft(a[i])
    mode+=1
    mode%=2
if mode==1:
  b=list(b)
  b=b[::-1]
print(*b)
