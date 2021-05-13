n=int(input())
p1=[float(0),float(0)]
p2=[float(100),float(0)]
cos=0.5
sin=0.866025404
def koh(d,p1,p2):
    if d==0:return True
    sx = (2 * p1[0] + p2[0]) / 3
    sy = (2 * p1[1] + p2[1]) / 3
    tx = (p1[0] + 2 * p2[0]) / 3
    ty = (p1[1] + 2 * p2[1]) / 3
    ux=(tx-sx)*cos-(ty-sy)*sin+sx
    uy=(tx-sx)*sin+(ty-sy)*cos+sy

    koh(d-1,p1,[sx,sy])
    print(sx, sy)
    koh(d-1,[sx,sy],[ux,uy])
    print(ux, uy)
    koh(d-1,[ux,uy],[tx,ty])
    print(tx,ty)
    koh(d-1,[tx,ty],p2)
print(p1[0],p1[1])
koh(n,p1,p2)
print(p2[0],p2[1])
