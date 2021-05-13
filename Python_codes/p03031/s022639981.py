N, M = map(int, input().split())
L = []
for _ in range(M):
  k, *S = map(int, input().split())
  L.append(S)
P = list(map(int, input().split()))
c = 0
for i in range(2**N):
  A = []
  for j in range(N):
    if (i>>j)&1:
      A.append(j+1)
  A = set(A)
  for i in range(M):
    if len(A&set(L[i]))%2!=P[i]:
      break
  else:
    c += 1
print(c)