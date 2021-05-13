def d(u):
 global t
 C[u]=0;D[u]=t;t+=1
 for v in M[u]:
  v=int(v)-1
  if C[v]:d(v)
 F[u]=t;t+=1
N=int(input());R=range(N)
M=[input().split()[2:]for _ in R]
C,D,F=[1]*N,[0]*N,[0]*N
t=1
for i in R:
 if C[i]:d(i)
for i in R:print(i+1,D[i],F[i])
