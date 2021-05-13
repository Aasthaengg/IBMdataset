n=int(input())

mat=[[0 for i in range(n)] for j in range(n)]
data=[[0 for i in range(n)] for j in range(n)]
for _ in range(n):
    x=list(map(int,input().split()))
    for j in range(n):
        mat[_][j]=x[j]
        data[_][j]=x[j]
def warshall_floyd(d):
    #d[i][j]=i番目の頂点からj番目の頂点までの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

newmat=warshall_floyd(mat)
if newmat==data:
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            ans+=data[i][j]*int(all(data[i][j]<data[i][k]+data[k][j] for k in range(i))&all(data[i][j]<data[i][k]+data[k][j] for k in range(i+1,j))&all(data[i][j]<data[i][k]+data[k][j] for k in range(j+1,n)))     
    print(ans)      
else:
    print(-1)