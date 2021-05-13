from collections import deque
N = int(input())
A = list(map(int, input().split()))

A.sort()
A = deque(A)
while len(A) > 1:
  s = []
  for i in range(len(A)-1):
    div = A[-1] % A[0]
    A.pop()
    if div != 0:
      s.append(div)
  s.append(A[0])
  s.sort()
  A = deque(s)
print(*A)
