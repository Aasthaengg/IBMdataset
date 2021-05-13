h,w=map(int,input().split())
d=[list(map(int,input().split())) for _ in range(10)]
e=[list(map(int,input().split())) for _ in range(h)]
def warshall_floyd(d,n):
    #d[i][j]=i番目の頂点からj番目の頂点までの最短距離
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
d=warshall_floyd(d,9)
ans=0
for i in range(h):
    for j in range(w):
        if e[i][j]>=0:
            ans+=d[e[i][j]][1]
print(ans)