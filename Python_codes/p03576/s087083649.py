n,K=map(int,input().split())
xy=[]
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
    xy.append([a,b])
x.sort()
y.sort()
data=[[0]*(n+1) for i in range(n+1)]
for u in xy:
    a,b=u
    X=x.index(a)
    Y=y.index(b)
    data[X][Y]=1
for i in range(n):
    for j in range(1,n):
        data[i][n-1-j]+=data[i][n-j]
for i in range(1,n):
    for j in range(n):
        data[n-i-1][j]+=data[n-i][j]
ans=float("inf")
for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            for l in range(k+1,n):
                if data[i][k]+data[j+1][l+1]-data[i][l+1]-data[j+1][k]>=K:
                    ans=min(ans,(x[j]-x[i])*(y[l]-y[k]))
print(ans)