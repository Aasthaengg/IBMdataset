x,y = map(int,input().split())
if 0<=x<=y:
    print(y-x)
elif 0<y<=x:
    print(2+x-y)
elif y==0 and x>=y:
    print(1+x-y)
elif y<=x<0:
    print(2+x-y)
elif y<x==0:
    print(x-y+1)
elif x<y<=0:
    print(y-x)
elif x<0 and y>0:
    if y>=abs(x):
        print(1+y+x)
    else:
        ans = min(-y-x+1,y-x)
        print(ans)
elif y<0 and x>0:
    if abs(y)>=x:
        print(abs(y)-x+1)
    else:
        print(1+y+x)