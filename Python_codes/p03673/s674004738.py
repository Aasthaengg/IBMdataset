N = int(input())
A = list(map(int,input().split()))

from collections import deque

q = deque([])

for i in range(N):
  if i % 2:
    q.appendleft(A[i])
  else:
    q.append(A[i])
    
if N % 2:
  q = list(q)[::-1]
  
print(*q)