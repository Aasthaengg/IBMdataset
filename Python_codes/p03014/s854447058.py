h,w=map(int,input().split())
field=[list(input()) for i in range(h)]

l=[[0]*w for i in range(h)]
r=[[0]*w for i in range(h)]
u=[[0]*w for i in range(h)]
d=[[0]*w for i in range(h)]

for i in range(h):
    for j in range(w):
        if field[i][j]=="#":
            l[i][j]=0
        elif j==0:
            l[i][j]=1
        else:
            l[i][j]=l[i][j-1]+1

for i in range(h):
    for j in reversed(range(w)):
        if field[i][j]=="#":
            r[i][j]=0
        elif j==w-1:
            r[i][j]=1
        else:
            r[i][j]=r[i][j+1]+1

for i in range(h):
    for j in range(w):
        if field[i][j]=="#":
            u[i][j]=0
        elif i==0:
            u[i][j]=1
        else:
            u[i][j]=u[i-1][j]+1

for i in reversed(range(h)):
    for j in range(w):
        if field[i][j]=="#":
            d[i][j]=0
        elif i==h-1:
            d[i][j]=1
        else:
            d[i][j]=d[i+1][j]+1

ans=0
for i in range(h):
    for j in range(w):
        tmp=l[i][j]+r[i][j]+u[i][j]+d[i][j]-3
        ans=max(ans,tmp)
print(ans)
