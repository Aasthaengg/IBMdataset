N = int(input())
A = [int(input()) for _ in range(N)]
A_max = 0
for i in range(N):
  A_max = max(A_max,A[i])
cnt = 0
for j in range(N):
  if A_max == A[j]:
    cnt += 1
  if cnt == 2:
    for _ in range(N):
      print(A_max)
    exit()
A[A.index(A_max)] = 0
A_second = 0
for l in range(N):
  A_second = max(A_second,A[l])
for m in range(N):
  print(A_second if A[m] == 0 else A_max)