n,m=map(int,input().split())
inf=float("inf")

data=[[inf]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    data[i][i]=0
lst=[]
for u in range(m):
    a,b,c=map(int,input().split())
    data[a][b]=c
    data[b][a]=c
    lst.append([a,b,c])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            data[i][j]=min(data[i][j],data[i][k]+data[k][j])

ans=0
for u in lst:
    a,b,c=u
    if data[a][b]!=c:
        ans+=1

print(ans)