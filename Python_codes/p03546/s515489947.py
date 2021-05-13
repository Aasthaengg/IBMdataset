h,w = map(int,input().split())
c = []
for i in range(10):
    ci = list(map(int,input().split()))
    c.append(ci)
A = []
for i in range(h):
    a = list(map(int,input().split()))
    A.append(a)
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
c = warshall_floyd(c)
ans = 0
for i in range(h):
    for j in range(w):
        if A[i][j] == -1:
            continue
        else:
            ans+=c[A[i][j]][1]
print(ans)