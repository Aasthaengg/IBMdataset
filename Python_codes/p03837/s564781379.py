# cadidates of no shortest paths
n, m = map(int, input().split())

d = [[float("inf") for i in range(n + 1)] for i in range(n + 1)]
edge_data=[]
connect={i:[] for i in range(1,n+1)}
for i in range(m):
    x, y, z = map(int, input().split())
    # 有向グラフか無向グラフかによってここで場合わけが生じる
    d[x][y] = z
    d[y][x] = z
    connect[x].append(y)
    connect[y].append(x)    
    edge_data.append((x,y,z))
for i in range(n + 1):
    d[i][i] = 0  # 自身のところに行くコストは０


def warshall_floyd(d):
    # d[i][j]=i番目の頂点からj番目の頂点までの最短距離
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

warshall_floyd(d)

#最短距離を求めた
cnt=0
for some in edge_data:
    x,y,z=some[0],some[1],some[2]
    if d[x][y]<z:
        cnt+=1
print(cnt)
    


