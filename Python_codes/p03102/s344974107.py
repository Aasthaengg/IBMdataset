N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
A = []

for i in range(N):
  tmp = list(map(int, input().split()))
  A.append(tmp)

test = 0
cnt = 0

for i in range(N):
  for j in range(M):
    test += A[i][j]*B[j]
  if test > -C:
    cnt += 1
  test = 0
print(cnt)