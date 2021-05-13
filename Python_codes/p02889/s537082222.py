def warshall_floid(d):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    return d

n,m,l = map(int,input().split())
d = [[10**12]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    d[a][b] = c
    d[b][a] = c
d = warshall_floid(d)
for i in range(1,n+1):
    for j in range(1,n+1):
        if d[i][j] <= l:
            d[i][j] = 1
        else:
            d[i][j] = 10**12
d = warshall_floid(d)
q = int(input())
for i in range(q):
    s,t = map(int,input().split())
    if d[s][t] >= 10**12:
        print(-1)
    else:
        print(d[s][t]-1)
