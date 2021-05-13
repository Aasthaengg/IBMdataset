n,k=map(int,input().split())
x,y=[[0,0] for i in range(n)],[[0,0] for i in range(n)]
xy=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    x_sub,y_sub=xy[i]
    x[i][0]=x_sub
    x[i][1]=i
    y[i][0]=y_sub
    y[i][1]=i
x.sort()
y.sort()
ans=(10**18)*5
for i1 in range(n):
    for l1 in range(n-i1,1,-1):
        for i2 in range(n):
            for l2 in range(n-i2,1,-1):
                x_sub1=x[i1][0]
                x_sub2=x[i1+l1-1][0]
                y_sub1=y[i2][0]
                y_sub2=y[i2+l2-1][0]
                z=[0]*n
                for i in range(n):
                    if x_sub1<=xy[i][0]<=x_sub2 and y_sub1<=xy[i][1]<=y_sub2:
                        z[i]=1
                if sum(z)>=k:
                    ans=min((x_sub2-x_sub1)*(y_sub2-y_sub1),ans)
print(ans)
