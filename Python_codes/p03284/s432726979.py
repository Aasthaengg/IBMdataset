A = list(map(int, input().split()))
B = A[0] % A[1]
if B == 0:
  print(0)
else:
  print(1)