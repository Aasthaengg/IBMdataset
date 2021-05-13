from math import log2
N = int(input())
a = list(map(int, input().split()))
Maxa = max(a)
if(Maxa == 0):
  for i in range(N):
    print(0, end = " ")
else:
  J = int(log2(Maxa)) + 1
  A = [format(x, 'b').zfill(J) for x in a]
  S = [0] * J
  for j in range(J):
    for i in range(N):
      S[j] += int(A[i][j])
    S[j] %= 2

  X = [""] * N
  for i in range(N):
    for j in range(J):
      X[i] += str(int((int(A[i][j]) != S[j])))
    print(int(X[i], 2), end = " ")