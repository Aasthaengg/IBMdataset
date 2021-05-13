x,y=map(int,input().split())

X=abs(x)
Y=abs(y)

if x<y:
    if x*y>0:
        print(abs(X-Y))
    elif x*y==0:
        print(abs(X-Y))
    else:
        print(abs(X-Y)+1)
else:
    if x*y>0:
        print(abs(X-Y)+2)
    elif x*y==0:
        print(abs(X-Y)+1)
    else:
        print(abs(X-Y)+1)