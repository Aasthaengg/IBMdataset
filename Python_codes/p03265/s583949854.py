x1,y1,x2,y2 = map(int,input().split())
v = (-(y2-y1),x2-x1)
print(x2+v[0],y2+v[1],x1+v[0],y1+v[1])
