N = int(input())
T = input().split(' ')
T = [int(T[i]) for i in range(N)]
SUM = sum(T)
M = int(input())
for i in range(M):
  P, X = input().split(' ')
  P = int(P)
  X = int(X)
  A = SUM - T[P-1] + X
  print(A)
