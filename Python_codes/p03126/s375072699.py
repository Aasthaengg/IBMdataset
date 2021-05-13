n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
a=[0]*m
for i in range(n):
    for j in range(l[i][0]):
        a[l[i][j+1]-1]+=1
ans=0
for i in range(m):
    if a[i]==n:
        ans+=1
print(ans)