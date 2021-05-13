w,h,n=map(int,input().split())
li=[list(map(int, input().split())) for _ in range(n)]
hi=[0]*h;wi=[0]*w
for i in range(n):
    x=li[i][0]
    y=li[i][1]
    if li[i][2]==1:
        for j1 in range(x):
            wi[j1]=1
    elif li[i][2]==2:
        for j2 in range(x,w):
            wi[j2]=1
    elif li[i][2]==3:
        for j3 in range(y):
            hi[j3]=1
    else:
        for j4 in range(y,h):
            hi[j4]=1
res=w*h
res-=sum(wi)*h
res-=(sum(hi))*(w-sum(wi))
print(res)