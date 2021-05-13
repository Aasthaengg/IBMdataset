h,w=map(int,input().split())
c=[list(map(int,input().split())) for _ in range(10)]
for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j]=min(c[i][j],c[i][k]+c[k][j])
ans=0
for _ in range(h):
    for i in map(int,input().split()):
        if i!=-1:
            ans+=c[i][1]
print(ans)