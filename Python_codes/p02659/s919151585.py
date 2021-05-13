import math

A, B = input().split()

A = int(A)
B_p = int(B.split(".")[0])
B_c = int(B.split(".")[1])

if (A == 0) or (B == 0):
  print(0)
else:
  ABp = A * B_p
  ABc = int(str(A * B_c)[:-2]) if len(str(A * B_c))>2 else 0
  print(ABp+ABc)