A = sorted(list(map(int, input().split())))
if A[2] % 2 == 0:
  print(0)
else:
  print(A[0] * A[1])