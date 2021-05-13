from collections import deque
N, M = map(int, input().split())
B = [[] for i in range(N)]
C = [0 for i in range(N)]
for i in range(M):
  a, b = map(int, input().split())
  B[a-1].append(b)
  B[b-1].append(a)
d = deque([1])
while len(d):
  p = d.pop()
  for q in B[p-1]:
    if C[q-1] == 0:
      C[q-1] = p
      d.appendleft(q)
print("Yes")
for i in range(1, N):
  print(C[i])