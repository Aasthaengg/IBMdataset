import math

def plot(x,y):
    print(f'{x:.8f} {y:.8f}')

def koch(n,ax,ay,bx,by):
    if n==0:
        plot(ax,ay)
        return
    
    sx=(2*ax+bx)/3
    sy=(2*ay+by)/3
    tx=(ax+2*bx)/3
    ty=(ay+2*by)/3
    ux=((tx-sx)*math.cos(math.radians(60)))-((ty-sy)*math.sin(math.radians(60)))+sx
    uy=((tx-sx)*math.sin(math.radians(60)))+((ty-sy)*math.cos(math.radians(60)))+sy

    koch(n-1, ax,ay, sx,sy)
    koch(n-1, sx,sy, ux,uy)
    koch(n-1, ux,uy, tx,ty)
    koch(n-1, tx,ty, bx,by)
    
n=int(input())
koch(n, 0,0, 100,0)    
plot(100,0)

