N, M = map(int, input().split())
A = []
B = []
for i in range(N):
  A.append(list(map(int, input().split())))
for i in range(M):
  B.append(list(map(int, input().split())))
for i in range(N):
  ans = M
  d = abs(A[i][0] - B[M-1][0]) + abs(A[i][1] - B[M-1][1])
  for j in range(M-2, -1, -1):
    dis = abs(A[i][0] - B[j][0]) + abs(A[i][1] - B[j][1])
    if d >= dis:
      d = dis
      ans = j + 1
  print(ans)