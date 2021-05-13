h,w=map(int,input().split())
ans=[float("inf") for i in range(10)]
p=[]
a=[]
for i in range(10):
    p.append(list(map(int,input().split())))
for i in range(h):
    a.append(list(map(int,input().split())))
for i in range(10):
    for j in range(10):
        for k in range(10):
            p[j][k]=min(p[j][i]+p[i][k],p[j][k])
ans=float("inf")
tmp=0
for j in range(h):
    for k in range(w):
        if a[j][k]!=-1:
            tmp+=p[a[j][k]][1]
print(tmp)