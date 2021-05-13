# ワーシャル-フロイド法
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,w = map(int,input().split()) #n:頂点数　w:辺の数
d = [[float('inf') for i in range(n+1)] for i in range(n+1)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
W = []
for i in range(w):
    x,y,z = map(int,input().split())
    W.append((x,y,z))
    d[x][y] = z
    d[y][x] = z
for i in range(n+1):
    d[i][i] = 0 #自身のところに行くコストは０
a = 0
warshall_floyd(d)
for i in range(w):
    x,y,z = W[i][0],W[i][1],W[i][2]
    if d[x][y] < z:
        a += 1
print(a)