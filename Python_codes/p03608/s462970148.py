from itertools import permutations
n,m,r=map(int,input().split())
rlis=list(map(int,input().split()))
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
d=[[10**10]*n for _ in range(n)]
for _ in range(m):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  d[a][b]=c
  d[b][a]=c
for i in range(n):
  d[i][i]=0
dist=warshall_floyd(d)
rlisp=list(permutations(rlis,r))
ans=10**10
for i in rlisp:
  cnt=0
  for j in range(r-1):
    cnt+=dist[i[j]-1][i[j+1]-1]
  ans=min(ans,cnt)
print(ans)