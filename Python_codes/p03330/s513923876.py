n,c=map(int,input().split())
d=[]
for i in range(c):
    d.append(list(map(int,input().split())))
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
p=[[0 for j in range(c)] for i in range(3)]
for i in range(n):
    for j in range(n):
        p[(i+1+j+1)%3][l[i][j]-1]+=1
ans=10**10
for i in range(c):
    for j in range(c):
        for k in range(c):
            if i!=j and i!=k and j!=k:
                t=0
                for x in range(c):
                    t+=d[x][i]*p[0][x]
                    t+=d[x][j]*p[1][x]
                    t+=d[x][k]*p[2][x]
                ans=min(ans,t)
print(ans)   