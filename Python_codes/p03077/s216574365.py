N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
X = min(A, B, C, D, E)
if X >= N:
  print(5)
else:
  if N%X == 0:
    print(4+N//X)
  else:
    print(5+N//X)