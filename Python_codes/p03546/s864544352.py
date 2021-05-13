def warshall_floyd(n, d):
    #d[i][j]: iからjへの最短距離
    for k in range(n): #経由する頂点
        for i in range(n): #始点
            for j in range(n): #終点
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

h,w=map(int,input().split())
c=[list(map(int,list(input().split()))) for _ in range(10)]
a=[list(map(int,list(input().split()))) for _ in range(h)]
e=[x[1] for x in warshall_floyd(10,c)]

ans=0
for i in range(h):
    for j in range(w):
        if a[i][j]!=-1:
            ans+=e[a[i][j]]
print(ans)