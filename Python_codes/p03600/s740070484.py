from copy import deepcopy
def solve():
  ans = 0
  N = int(input())
  A = [list(map(int, input().split())) for _ in range(N)]
  d = deepcopy(A)
  D = deepcopy(A)
  #三重ループ
  for k in range(N):
    for i in range(N):
      if i==k:
        continue
      for j in range(N):
        if j==k:
          continue
        if d[i][k]+d[k][j]<=d[i][j]:
          d[i][j] = d[i][k]+d[k][j]
          D[i][j] = float('inf')
  for i in range(N): #ひとまず枝があるペアは枝の長さをセット
    for j in range(N):
      if D[i][j]<float('inf') and i>j:
        ans += A[i][j]
  #三重ループ
  for k in range(N):
    for i in range(N):
      for j in range(N):
        D[i][j] = min(D[i][j], D[i][k]+D[k][j])
  for i in range(N):
    for j in range(N):
      if D[i][j] != A[i][j]:
        return -1
  return ans
print(solve())