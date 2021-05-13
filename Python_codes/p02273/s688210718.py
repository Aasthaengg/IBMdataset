import math

n = int(input())

sin60 = math.sin(math.radians(60))
cos60 = math.cos(math.radians(60))
tan60 = math.tan(math.radians(60))

li = [[0, 0], [100, 0]]

for i in range(n):
    j = 0
    if n == 0:
        pass
    elif n == 1:
        li = [[0, 0], [100/3, 0], [50, 100/3*sin60], [100/3*2, 0], [100, 0]]
    else:
        for _ in range(4**i):
            sx = (li[j][0]*2 + li[j+1][0])/3
            sy = (li[j][1]*2 + li[j+1][1])/3
            tx = (li[j][0] + li[j+1][0]*2)/3
            ty = (li[j][1] + li[j+1][1]*2)/3
            ux = (tx-sx)*cos60 - (ty-sy)*sin60 + sx
            uy = (tx-sx)*sin60 + (ty-sy)*cos60 + sy
            li[j+1:0] = [[sx, sy], [ux, uy], [tx, ty]]
            j += 4

for i in range(len(li)):
    print('{:.8f} {:.8f}'.format(li[i][0], li[i][1]))
