from collections import deque
n = int(input())
A = deque(map(str, input().split()))
D = deque()
while A:
  x = A.popleft()
  D.append(x)
  if A:
    y = A.popleft()
    D.appendleft(y)
if n % 2 != 0:
  D.reverse()
print(" ".join(D))