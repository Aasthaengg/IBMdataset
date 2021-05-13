from copy import deepcopy
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


def warshall_floyd(d):
  #d[i][j]: iからjへの最短距離
  for k in range(N):
    for i in range(N):
      for j in range(N):
        d[i][j] = min(d[i][j],d[i][k] + d[k][j])
  return d

B = deepcopy(A)
#d = warshall_floyd(A)
#if B != d:
#  print(-1)
#  exit()

for i in range(N):
  for j in range(N):
    for k in range(N):
      if i == j or j == k or k == i:
        continue
      if A[i][k] + A[k][j] < A[i][j]:
        print(-1)
        exit()
      elif A[i][k] + A[k][j] == A[i][j]: 
        B[i][j] = 0

ans = 0
for i in range(N):
  for j in range(i+1, N):
    ans += B[i][j]

print(ans)