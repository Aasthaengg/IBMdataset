import itertools

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,m,r = map(int,input().split()) #n:頂点数  w:辺の数
arr=list(map(int,input().split()))

d = [[float("inf")]*n for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    x,y,z = map(int,input().split())
    x-=1
    y-=1
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０

table=warshall_floyd(d)

ans=float('inf')
for lst in itertools.permutations(arr,r):
  cnt=0
  for i in range(r-1):
    cnt+=table[lst[i]-1][lst[i+1]-1]

  ans=min(ans,cnt)


print(ans)