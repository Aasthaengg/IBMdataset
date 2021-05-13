n,m,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
xx=max(x)
yy=min(y)
t1=max(X,xx)
t2=min(Y,yy)
if t1<t2:
    print("No War")
else:
    print("War")