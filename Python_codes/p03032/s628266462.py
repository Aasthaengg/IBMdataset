import heapq
from collections import deque
from copy import deepcopy

n,k = map(int,input().split())
V = list(map(int,input().split()))

dq = deque()
dq.extend(V)
INF = 10**10

ans = -INF
for i in range(k+1):
  for j in range(k+1-i):           
    que = deepcopy(dq)
    a = []    
    
    if i+j <= n:
      for l in range(i):      
        heapq.heappush(a,que.popleft())
      for r in range(j):
        heapq.heappush(a,que.pop())    
      
      ans = max(ans,sum(a))        
      for ki in range(k-i-j):   
        if len(a) > 0:
          heapq.heappop(a)
        ans = max(ans,sum(a))        
        
if ans != -INF:          
  print(ans)
else:
  print(0)  