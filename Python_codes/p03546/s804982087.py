h,w=map(int,input().split())
c=[[0]*10 for _ in range(10)]
for i in range(10):
    c[i]=list(map(int, input().split()))

a=[[0]*w for _ in range(h)]
for i in range(h):
    a[i]=list(map(int, input().split()))


def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    return d


ans=0
for i in range(h):
    for j in range(w):
        if a[i][j]>-1:
            ans+=warshall_floyd(c)[a[i][j]][1]
print(ans)