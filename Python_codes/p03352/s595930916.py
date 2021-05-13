import math
X=int(input())

A=[1]
for b in range(2,32):
  for p in range(2,10):
    if b**p>X:
      break
    elif b**p not in A:
      A.append(b**p)
print(max(A))

