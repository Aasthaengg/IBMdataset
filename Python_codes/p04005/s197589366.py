ABC = list(map(int, input().split()))

ABC.sort()

A, B, C = ABC
if A * B * C % 2 == 0:
  print(0)
else:
  print(A * B)
