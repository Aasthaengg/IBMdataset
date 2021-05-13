import copy
n,ma,mb=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(n)]
l=10*n
inf=float("inf")
data=[[inf]*(l+1) for i in range(l+1)]
data[0][0]=0
for u in abc:
    a,b,c=u
    h=copy.deepcopy(data)
    for i in range(l-a+1):
        for j in range(l-b+1):
            if data[i][j]!=inf:
                h[i+a][j+b]=min(h[i+a][j+b],data[i][j]+c)
    data=h
k=1
ans=inf
while ma*k<=l and mb*k<=l:
    if data[ma*k][mb*k]!=inf:
        ans=min(ans,data[ma*k][mb*k])
    k+=1
if ans!=inf:
    print(ans)
else:
    print(-1)