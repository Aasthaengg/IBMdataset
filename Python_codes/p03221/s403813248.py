N, M = map(int, input().split())
A = []
B = [[] for i in range(N)]
for i in range(M):
  P, Y = map(int, input().split())
  A.append([P, Y])
  B[P-1].append(Y)
for i in range(N):
  B[i].sort()
d = {}
for i in range(N):
  for y in range(len(B[i])):
    d[(i+1, B[i][y])] = y + 1
for i in range(M):
  print('{:0=6}'.format(A[i][0]) + '{:0=6}'.format(d[(A[i][0], A[i][1])]))