n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = [A[i] - B[i] for i in range(n)]
C.sort()

if sum(C)<0:
  print(-1)
  exit()
  
ans = 0

from collections import deque
C = deque(C)
c = 0
while C:
  nc = C.popleft()
  if nc >=0:
    break
  c+= nc
  ans += 1
  while c<0:
    c+=C.pop()
    ans += 1
print(ans)

