from collections import deque
N, Q = map(int, input().split())
A = [[] for i in range(N)]
for i in range(N - 1):
  a, b = map(int, input().split())
  A[a-1].append(b-1)
  A[b-1].append(a-1)
B = [[0, -1] for i in range(N)]
for i in range(Q):
  p, x = map(int, input().split())
  B[p-1][0] += x
d = deque([0])
while len(d) != 0:
  x = d.popleft()
  for a in A[x]:
    if a == B[x][1]:
      continue
    B[a][1] = x
    B[a][0] += B[x][0]
    d.append(a)
for i in range(N):
  print(B[i][0], end = "")
  if i != N - 1:
    print(" ", end = "")