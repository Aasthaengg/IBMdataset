import math
n = int(input())
A = []
for _ in range(n):
  A.append(int(input()))
B = sorted(A)
m = max(A)  
for a in A:
  if a < m:
    print(m)
  else:
    print(B[-2])

