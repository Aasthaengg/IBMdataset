N, M, X = input().split()
N = int(N)
M = int(M)
X = int(X)
A = input().split()
A = [int(A[i]) for i in range(M)]
A.append(X)
A = sorted(A)
if M/2 > A.index(X):
  print(A.index(X))

elif  M/2 < A.index(X):
  print(int(M-A.index(X)))