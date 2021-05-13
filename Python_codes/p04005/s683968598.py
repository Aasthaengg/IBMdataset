A = list(map(int, input(). split()))
A.sort()
if (A[0]*A[1]*A[2])%2 == 1:
  print(A[0]*A[1])
else:
  print(0)