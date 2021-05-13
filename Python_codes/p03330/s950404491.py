n,c=map(int,input().split())
d=[list(map(int,input().split())) for i in range(c)]
grid=[list(map(int,input().split())) for i in range(n)]
lst=[[0]*(c+1) for i in range(3)]
for i in range(n):
    for j in range(n):
        num=grid[i][j]
        a=(i+j)%3
        lst[a][num]+=1
li=[[0]*(c+1) for i in range(3)]
for i in range(3):
    u=lst[i]
    for j in range(1,c+1):
        count=0
        for k in range(1,c+1):
            count+=d[k-1][j-1]*u[k]
        li[i][j]=count
ans=float("inf")
for i in range(1,c+1):
    for j in range(1,c+1):
        for k in range(1,c+1):
            if i!=j and j!=k and k!=i:
                a=li[0][i]+li[1][j]+li[2][k]
                ans=min(ans,a)
print(ans)