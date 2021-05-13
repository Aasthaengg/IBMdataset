from collections import deque
N, M = map(int, input().split())
A = [[] for i in range(N)]
for i in range(M):
  a, b = map(int, input().split())
  A[a-1].append(b - 1)
  A[b-1].append(a - 1)
B = [0 for i in range(N)]
cnt = 0
for i in range(N):
  if B[i] == 0:
    cnt += 1
    B[i] = cnt
    D = deque([i])
    while len(D) > 0:
      d = D.pop()
      for j in A[d]:
        if B[j] == 0:
          B[j] = cnt
          D.append(j)
print(cnt - 1)