import math

def koch(n, p1, p2):
    if n == 0:
        return
    
    sx = 2*p1[0]/3 + p2[0]/3
    sy = 2*p1[1]/3 + p2[1]/3
    tx = p1[0]/3 + 2*p2[0]/3
    ty = p1[1]/3 + 2*p2[1]/3
    ux = (tx - sx)*math.cos(math.radians(60))  - (ty - sy)*math.sin(math.radians(60)) + sx
    uy = (tx - sx)*math.sin(math.radians(60)) + (ty - sy)*math.cos(math.radians(60)) + sy
    koch(n-1, p1, [sx, sy])
    print(sx, sy)
    koch(n-1, [sx, sy], [ux, uy])
    print(ux, uy)
    koch(n-1, [ux, uy], [tx, ty])
    print(tx, ty)
    koch(n-1, [tx, ty], p2)
    
    
    
    
    
    
n = int(input())
#問題文より，　端点がp1 = (0,0), p2 =(100,0)と指定されている
p1 = [0, 0]
p2 = [100, 0]
print(p1[0], p1[1])
koch(n, p1, p2)
print(p2[0], p2[1])
