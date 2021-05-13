N = int(input())
A = list(map(int, input().split()))
if N % 2 == 0:
  for i in range(N-1, -1, -2):
    print(A[i], end = "")
    print(" ", end = "")
  for i in range(0, N, 2):
    print(A[i], end = "")
    if i != N - 2:
      print(" ", end = "")
    else:
      print("")
else:
  for i in range(N-1, -2, -2):
    print(A[i], end = "")
    print(" ", end = "")
  for i in range(1, N, 2):
    print(A[i], end = "")
    if i != N - 2:
      print(" ", end = "")
    else:
      print("")