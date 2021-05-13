h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

from collections import deque
q=deque([])
for i in range(n):
  for j in range(a[i]):
    q.append(i+1)

cnt=0
for i in range(h):
  s=[]
  for i in range(w):
    p=q.popleft()
    s.append(p)
  cnt+=1
  if cnt%2==0:
    s.reverse()
    for num in s:
      print(num,end=" ")
    print()
  else:
    for num in s:
      print(num,end=" ")
    print()
    
