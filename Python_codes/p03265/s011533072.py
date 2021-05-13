x1,y1,x2,y2=map(int,input().split())
hen=((x1-x2)**2+(y1-y2)**2)**(0.5)
dx=x2-x1
dy=y2-y1
print(x2-dy,dx+y2,x2-dy-dx,dx+y2-dy)