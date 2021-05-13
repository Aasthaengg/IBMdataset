w,h,n=map(int,input().split())

x_mx=w
x_mn=0
y_mx=h
y_mn=0
for i in range(n):
    x,y,a=map(int,input().split())
    if a==1:
        x_mn=max(x_mn,x)
    elif a==2:
        x_mx=min(x_mx,x)
    elif a==3:
        y_mn=max(y_mn,y)
    else:
        y_mx=min(y_mx,y)

ans=(x_mx-x_mn)*(y_mx-y_mn)
if x_mx-x_mn<=0 or y_mx-y_mn<=0:
    ans=0
print(max(ans,0))