L=list()
R=list()
N,M=map(int,input().split())
for i in range(N):
  a,b=map(int,input().split())
  L.append([a,b])
for i in range(M):
  a,b=map(int,input().split())
  R.append([a,b])
ans=[0]*M
for i in range(N):
  K=[0]*M
  a,b=L[i]
  for j in range(M):
    K[j]=abs(a-R[j][0])+abs(b-R[j][1])
  s=min(K)
  q=K.index(s)
  print(q+1)