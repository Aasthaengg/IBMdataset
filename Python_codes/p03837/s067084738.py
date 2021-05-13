import sys
sys.setrecursionlimit(1000001)

n, m = map(int, input().rstrip().split())
dist = [[500000 for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        if (i==j):
            dist[i][j]=0

a = []
b = []
c = []

for i in range(m):
    x, y, z = map(int, input().rstrip().split())
    dist[x-1][y-1] =  min(dist[x-1][y-1], z)
    dist[y-1][x-1] =  min(dist[x-1][y-1], z)
    a.append(x-1)
    b.append(y-1)
    c.append(z)
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
#print(dist)
result = m

for i in range(m):
    for j in range(n):
        if dist[j][a[i]] + c[i] == dist[j][b[i]]:
            result -= 1
            break

print(result)