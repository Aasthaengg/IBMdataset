from collections import deque
n=int(input())
a=list(input().split())
b=deque()

for i in range(1,n+1):
  if (i%2==1 and n%2==0) or (i%2==0 and n%2==1):
    b.append(a[i-1])
  else:
    b.appendleft(a[i-1])
print(" ".join(b))