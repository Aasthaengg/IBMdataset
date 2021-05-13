N,M,Q = map(int,input().split())
m = [[0 for i in range(N+1)] for i in range(N+1)]
for i in range(M):
  l,r = map(int,input().split())
  m[l][r] += 1
for i in range(N+1):
  for j in range(N):
    m[i][j+1] += m[i][j]
for i in range(N):
  for j in range(N+1):
    m[i+1][j] += m[i][j]    

p = [0]
q = [0]
for i in range(Q):
  a,b = map(int,input().split())
  p.append(a)
  q.append(b)


for i in range(1,Q+1):
  print(m[q[i]][q[i]]+m[p[i]-1][p[i]-1]-m[q[i]][p[i]-1]-m[p[i]-1][q[i]])
