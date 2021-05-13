N = int(input())
D = {i: [0] for i in range(N)}
for i in range(N-1):
  a, b = map(int, input().split())
  D[a-1].append(b-1)
  D[a-1][0] += 1
  D[b-1].append(a-1)
  D[b-1][0] += 1
m = 0
nod = -1
for i in D:
  if m < D[i][0]:
    m = D[i][0]
    nod = i
c = list(map(int, input().split()))
c.sort(reverse=True)
pnt = 0
cnt = 1
p = [nod]
L = [-1 for _ in range(N)]
L[nod] = c[0]
while cnt < N:
  n = cnt
  for i in range(pnt, cnt):
    for j in range(1, D[p[i]][0]+1):
      if L[D[p[i]][j]] == -1:
        L[D[p[i]][j]] = c[cnt]
        cnt += 1
        p.append(D[p[i]][j])
  pnt = n
S = 0
for i in D:
  for j in range(1, D[i][0]+1):
    S += min(L[i], L[D[i][j]])
print(S//2)
for i in range(N):
  print(L[i], end = ' '*(i != N - 1))
print()