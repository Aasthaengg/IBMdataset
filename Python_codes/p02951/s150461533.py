A, B, C = map(int, input().split())
D = A - B
E = C - D
if E < 0:
  print(0)
else:
  print(E)