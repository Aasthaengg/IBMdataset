from collections import deque

n = int(input())
A = list(input().split())
B= deque()

for i in range(n):
  if i % 2:
    B.append(A[i])
  else:
    B.appendleft(A[i])
  
if n % 2 == 0:
  B.reverse()
  
print(" ".join(B))