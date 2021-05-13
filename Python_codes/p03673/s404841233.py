from collections import deque
N = int(input())
A = list(map(int, input().split()))
B = deque([])
c = 1
for a in A:
  if c:
    B.append(a)
  else:
    B.appendleft(a)
  c = 1-c
if N%2:
  B.reverse()
print(*B)