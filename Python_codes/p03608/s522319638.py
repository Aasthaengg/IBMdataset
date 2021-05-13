import copy
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
n,m,r=map(int,input().split())
R=list(map(int,input().split()))
for i in range(r):
  R[i]=R[i]-1
d=[[10**10]*n for i in range(n)] 
for i in range(m):
  a,b,c=map(int,input().split())
  a=a-1
  b=b-1
  d[a][b]=c
  d[b][a]=c
for i in range(n):
  d[i][i]=0
D=warshall_floyd(d)
s=1
S=[]
for i in range(1,r+1):
  s=s*i
  S.append(s)
ans=10**10
for i in range(s):
  RR=copy.copy(R)
  E=[]
  for j in range(r-1):
    E.append(RR[i//S[r-j-2]])
    RR.pop(i//S[r-j-2])
    i=i-S[r-j-2]*(i//S[r-j-2])
  E.append(RR[0]) 
  di=0
  for i in range(r-1):
    di=di+D[E[i]][E[i+1]]
  if di<ans:
    ans=di
print(ans)