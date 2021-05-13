import math
 
n=int(input())
 

a=math.sin(math.radians(60))
b=math.cos(math.radians(60))

 
def f(n,x1,x2,y1,y2):
    if n==0:
        return
 
    sx=(2*x1 + 1*x2) / 3
    sy=(2*y1 + 1*y2) / 3
    tx=(1*x1 + 2*x2) / 3
    ty=(1*y1 + 2*y2) / 3
    ux=(tx-sx)*b - (ty-sy)*a + sx
    uy=(tx-sx)*a + (ty-sy)*b + sy
 
    f(n-1,x1,sx,y1,sy)
    print(sx, sy)
    f(n-1,sx,ux,sy,uy)
    print(ux, uy)
    f(n-1,ux,tx,uy,ty)
    print(tx, ty)
    f(n-1,tx,x2,ty,y2)
 
 
print(0.00000000, 0.00000000)
f(n,0,100,0,0)
print(100.00000000, 0.00000000)
