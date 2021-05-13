N = int(input())
L = []
for _ in range(N):
  L.append([list(map(int, input().split())) for _ in range(int(input()))])
for ls in L:
  for l in ls:
    l[0] -= 1
M = 0
for i in range(1<<N):
  A, Normal = [], True
  for j in range(N):
    if (i>>j)&1:
      A.append(j)
  for a in A:
    for l in L[a]:
      if l[0] in A and l[1]==0:
        Normal = False
      if l[1]==1 and l[0] not in A:
        Normal = False
  if Normal:
    M = max(M, len(A))
print(M)