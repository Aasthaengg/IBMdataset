from math import*
a=(0,0)
b=(100,0)

def koch(n,ax,ay,bx,by):
    if n==0:
        return 0
    th=pi/3
    sx=(2*ax+bx)/3
    sy=(2*ay+by)/3
    tx=(ax+2*bx)/3
    ty=(ay+2*by)/3
    ux=(tx-sx)*cos(th)-(ty-sy)*sin(th)+sx
    uy=(tx-sx)*sin(th)+(ty-sy)*cos(th)+sy
    
    koch(n-1,ax,ay,sx,sy)
    print(sx,sy)
    koch(n-1,sx,sy,ux,uy)
    print(ux,uy)
    koch(n-1,ux,uy,tx,ty)
    print(tx,ty)
    koch(n-1,tx,ty,bx,by)


n=int(input())
print(*a)
koch(n,*a,*b)
print(*b)
