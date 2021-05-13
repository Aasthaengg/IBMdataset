import math
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
bottle = min([A, B, C, D, E])
if bottle < N:
  print(math.ceil(N/bottle)+4)
else:
  print(5)