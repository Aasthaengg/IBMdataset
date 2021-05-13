N=int(input())
import copy
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

  
cost=[list(map(int,input().split())) for i in range(N)]
D=copy.deepcopy(cost)
E=warshall_floyd(cost)
      
if D!=E: 
  print(-1)
  exit()
D=cost
for k in range(N):
  for i in range(N):
    for j in range(N):
      a,b,c=D[i][j],D[j][k],D[i][k]
      if a!=0 and b!=0 and c!=0:
        if D[i][j]==D[i][k]+D[k][j]:
          D[i][j]=0       
ans=0
for i in range(N):
  ans+=sum(D[i]) 
print(ans//2)
