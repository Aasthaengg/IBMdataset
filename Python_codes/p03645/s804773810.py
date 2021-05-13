N, M = map(int, input().split())
A = []
B = []
for i in range(M):
  a, b = map(int, input().split())
  if a == 1:
    A.append(b)
  if b == N:
    B.append(a)
C = list(set(A) & set(B))
ans = 'IMPOSSIBLE'
if len(C) > 0:
  ans = 'POSSIBLE'
print(ans)