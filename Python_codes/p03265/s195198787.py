x1, y1, x2, y2 = map(int,input().split())

dx = abs(x1-x2)
dy = abs(y1-y2)
if x1>x2 and y1>=y2 :
    print(x2+dy,y2-dx,x1+dy,y1-dx)
elif x1>=x2 and y1<y2 :
    print(x2-dy,y2-dx,x1-dy,y1-dx)
elif x1<=x2 and y1>y2 :
    print(x2+dy,y2+dx,x1+dy,y1+dx)
elif x1<x2 and y1<=y2 :
    print(x2-dy,y2+dx,x1-dy,y1+dx)