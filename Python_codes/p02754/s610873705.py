N, A, B = map(int, input().split())

s = A + B
q = N // s
r = N % s
if r == 0:
  print(A * q)
elif r < A:
  print(A*q + r)
else:
  print(A*q + A)