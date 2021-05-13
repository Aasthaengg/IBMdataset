from copy import deepcopy
n,m=map(int,input().split())
lst=[]
for i in range(n):
    x,y,z=map(int,input().split())
    lst.append([x,y,z])
ans=0
for i in range(8):
    switch=[0,0,0]
    for j in range(3):
        if (i>>j)&1:
            switch[j]=1
    tmp=deepcopy(lst)
    for j in range(n):
        p=0
        for k in range(3):
            if switch[k]==1:
                p+=tmp[j][k]
            else:
                p-=tmp[j][k]
        tmp[j].append(p)
    tmp=sorted(tmp,key=lambda x:x[3],reverse=True)
    x=0
    y=0
    z=0
    for j in range(m):
        x+=tmp[j][0]
        y+=tmp[j][1]
        z+=tmp[j][2]
    ans=max(ans,abs(x)+abs(y)+abs(z))
print(ans)