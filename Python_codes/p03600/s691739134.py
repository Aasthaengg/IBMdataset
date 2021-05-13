n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

def warshal_floyd(d):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        d[i][j] = min(d[i][j], d[i][k]+d[k][j])
  return d

import copy
B = copy.deepcopy(A)
B = warshal_floyd(B)

ans = 0
for i in range(n):
    for j in range(n):
        if B[i][j] < A[i][j]:
            print(-1)
            exit()
        else:
            for k in range(n):
                if k == i or k == j:
                    continue
                if B[i][j] == B[i][k] + B[k][j]:
                    break
            else:
                ans += A[i][j]
ans //=2
print(ans)