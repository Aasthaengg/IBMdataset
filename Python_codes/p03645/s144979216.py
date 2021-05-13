N, M = map(int, input().split())
A = [[] for i in range(N)]
for i in range(M):
  a, b = map(int, input().split())
  A[a-1].append(b)
  A[b-1].append(a)
ans = 'IMPOSSIBLE'
for aa in A[0]:
  if N in A[aa-1]:
    ans = 'POSSIBLE'
    break
print(ans)
