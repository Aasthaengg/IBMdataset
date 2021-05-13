x,y=map(int,input().split())
if 0<=x<y:
    print(abs(y-x))
elif -y<x<y:
    print(abs(y+x)+1)
elif x<=-y<0:
    print(abs(-y-x)+1)
elif x<y<=0:
    print(abs(y-x))
elif 0<y<x:
    print(abs(-y+x)+2)
elif y==0 and y<x:
    print(abs(x)+1)
elif -x<=y<0:
    print(1+abs(y+x))
elif 0<=x<-y:
    print(abs(-y-x)+1)
else:
    print(abs(-y+x)+2)
