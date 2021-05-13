N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [[0]*M]*N
count = 0
for i in range(N):
  A[i] =  list(map(int, input().split()))
for i in range(N):
  integer = 0
  for j in range(M):
    integer += A[i][j] * B[j]
  integer += C
  if integer > 0:
    count += 1
print(count)
