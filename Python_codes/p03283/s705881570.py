import sys
input=sys.stdin.readline
N,M,Q=map(int,input().split())

xmat=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
  l,r=map(int,input().split())
  xmat[l][r]+=1
#print(xmat)

smat=[[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
  for j in range(1,N+1):
    smat[i][j]=xmat[i][j]+smat[i][j-1]+smat[i-1][j]-smat[i-1][j-1]
#print(smat)

for i in range(Q):
  p,q=map(int,input().split())
  print(smat[q][q]-smat[p-1][q]-smat[q][p-1]+smat[p-1][p-1])