x,y,z=map(int,input().split())
xx=x+y
yy=y+z
zz=z+x
print(min(zz,xx,yy))