N, M = map(int, input().split())
A = []
B = []
for i in range(N):
  A.append(input())
for i in range(M):
  B.append(input())
f = 0
for i in range(N - M + 1):
  for j in range(N - M + 1):
    g = 0
    for k in range(M):
      for l in range(M):
        if A[i+k][j+l] != B[k][l]:
          g = 1
          break
      if g == 1:
        break
    if g == 0:
      print("Yes")
      f = 1
      break
  if f == 1:
    break
if f == 0:
  print("No")