n,m = map(int,input().split())
d =[[float('inf') for _ in range(n)] for _ in range(n)]
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
    edges.append((a,b,c))
for i in range(n):
    d[i][i] = 0
# warshall_floyd
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])
s = set()
for i in range(n):
    for j in range(m):
        if d[i][edges[j][0]-1] + edges[j][2] == d[i][edges[j][1]-1]:
            s.add(j)
print(m-len(s))