def d(u):
 global t
 C[u]=0;t+=1;D[u]=t
 for v in R:
  if M[u][v]and C[v]:d(v)
 t+=1;F[u]=t
N=int(input());R=range(N)
M=[[0]*N for _ in R]
for e in[input().split()for _ in R]:
 for v in e[2:]:M[int(e[0])-1][int(v)-1]=1
C,D,F=[1]*N,[0]*N,[0]*N
t=0
for i in R:
 if C[i]:d(i)
for i in R:print(i+1,D[i],F[i])
