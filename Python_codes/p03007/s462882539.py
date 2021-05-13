from collections import deque
N = int(input())
A = [int(i) for i in input().split()]
A.sort()
A = deque(A)
m = A.popleft()
ans = []
while len(A)>1:
  if A[-2]<=0:
    break
  x = A.pop()
  ans += [(m,x)]
  m = m-x
for i in range(len(A)-1):
  ans += [(A[-1],A[i])]
  A[-1] = A[-1]-A[i]

ans += [(A[-1],m)]
print(A[-1]-m)
for a in ans:
  print(*a)