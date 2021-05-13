n,m,q=map(int,input().split())
data=[[0 for i in range(n+1)] for j in range(n+1)]
for _ in range(m):
    l,r=map(int,input().split())
    data[l][r]+=1

for i in range(n+1):
    for j in range(1,n+1):
        data[i][j]+=data[i][j-1]
for i in range(n+1):
    for j in range(1,n+1):
        data[j][i]+=data[j-1][i]

for _ in range(q):
    x,y=map(int,input().split())
    print(data[y][y]-data[x-1][y]-data[y][x-1]+data[x-1][x-1])
