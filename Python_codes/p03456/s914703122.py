import math
A = list(map(int, input().split()))

B = str(A[0]) + str(A[1])
C = int(B)

D = math.sqrt(C)

if D.is_integer():
  print('Yes')
else:
  print('No')