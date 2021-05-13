n=int(input())
d=[list(map(int,input().split())) for i in range(n)]
def fill(l,x):
    w=len(l[0])
    return [[x]*(w+2)]+[[x]+i+[x] for i in l]+[[x]*(w+2)]
def swap(a,b):
    if a>b:
        return b,a
    return a,b
d=fill(d,0)
edge=[{} for i in range(n+1)]
for j in range(1,n+1):
    for i in range(j+1,n+1):
        edge[j][i]=d[i][j]
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if  d[i][j]>d[i][k]+d[k][j]:
                print(-1)
                quit()
            elif d[i][j]==d[i][k]+d[k][j]:
                if k==i or k==j:
                    continue
                x,y=swap(i,j)
                if y in edge[x]:
                    del edge[x][y]
ans=0
for i in edge:
    ans+=sum(i.values())
print(ans)