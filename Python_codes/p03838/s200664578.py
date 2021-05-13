x,y=map(int,input().split())
X=abs(x)
Y=abs(y)
if X<Y:
    if x<y:
        if x*y>=0:
            p=y-x
        else:
            p=y-(-x)+1      
    else:
        if x*y>0:
            p=(-y)-(-x)+2
        else:
            p=(-y)-x+1

else:
    if x<y:
        if x*y>=0:
            p=y-x
        else:
            p=(-y)-x+1
    else:
        if x*y>0:
            p=(-y)-(-x)+2
        else:
            p=y-(-x)+1
print(p)