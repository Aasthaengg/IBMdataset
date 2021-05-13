from subprocess import call
call(('pypy3','-c',"""N,M,R=map(int,input().split())
r=list(map(int,input().split()))
A=[list(map(int,input().split())) for i in range(M)]
d=[[float("inf")]*N for i in range(N)]

for a,b,c in A:
  d[a-1][b-1]=c
  d[b-1][a-1]=c 
  
for k in range(N):
  for i in range(N):
    for j in range(N):
      d[i][j]=min(d[i][j],d[i][k]+d[k][j])
      
import itertools 
ans=1000000000
for i in itertools.permutations(range(R),R):
  D=0
  for j in range(R-1):
    D+=d[r[i[j]]-1][r[i[j+1]]-1]
  ans=min(D,ans)
print(ans)
"""))
