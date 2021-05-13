from collections import deque
import heapq
N,K=map(int,input().split())
V=list(map(int,input().split()))
ans=0
  
for i in range(0,min(N,K)+1):
  for a in range(i+1):
    b=i-a
    
    l=0
    d=deque(V)
    minus=[]
    
    for j in range(a):
      p=d.popleft()
      l+=p
      if p<0:
        minus.append(p)
    for j in range(b):
      p=d.pop()
      l+=p
      if p<0:
        minus.append(p)
    heapq.heapify(minus)
    for j in range(min(len(minus),K-i)):
      k=heapq.heappop(minus)
      l-=k
    #print(a,b,l)
    ans=max(ans,l)
    
print(ans)