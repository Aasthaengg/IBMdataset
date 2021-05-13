N, M, X = map(int, input().split())
C = [list(map(int,input().split())) for _ in range(N)]
L = []

for i in range(2**N):
  A = [0 for _ in range(M+1)]
  for j in range(N):
    if i & (1<<j):
      for k in range(M+1):
        A[k] += C[j][k]
  flag = True
  for i in range(M):
    if A[i+1] < X:
      flag = False
  if flag:
    L.append(A[0])

if L == []:
  L.append(-1)
print(min(L))