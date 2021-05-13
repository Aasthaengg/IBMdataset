def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,m = map(int,input().split()) #n:頂点数  w:辺の数
lst=[]

d = [[float("inf")]*n for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    x,y,z = map(int,input().split())
    x-=1
    y-=1
    d[x][y] = z
    d[y][x] = z
    lst.append([x,y,z])
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０

table=warshall_floyd(d)
ans=0

for x,y,z in lst:
    if table[x][y]!=z:
        ans+=1


print(ans)