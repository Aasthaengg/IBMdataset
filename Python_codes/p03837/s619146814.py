def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,w = map(int,input().split()) #n:頂点数　w:辺の数

d = [[float("inf")]*n for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
x = [0]*w
y = [0]*w
z = [0]*w
for i in range(w):
    x[i],y[i],z[i] = map(int,input().split())
    d[x[i]-1][y[i]-1] = z[i]
    d[y[i]-1][x[i]-1] = z[i]
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
d = warshall_floyd(d)

res = 0
for i in range(w):
    if z[i] > d[x[i]-1][y[i]-1]:
        res += 1
print(res)