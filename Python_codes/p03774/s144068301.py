n,m=map(int,input().split())
stu=[[0,0] for i in range(n)]
po=[[0,0] for i in range(m)]
for i in range(n):
    a,b=map(int,input().split())
    stu[i][0]=a
    stu[i][1]=b
for i in range(m):
    c,d=map(int,input().split())
    po[i][0]=c
    po[i][1]=d
ans=[]
for i in range(n):
    x=stu[i][0]
    y=stu[i][1]
    dis=[]
    for j in range(m):
        dis.append(abs(x-po[j][0])+abs(y-po[j][1]))
    ans.append(dis.index(min(dis)))
for i in range(n):
    print(ans[i]+1)

