import math

def coh(n, p1, p2, pt_list, m):
    if n>m:
        return 
    x1, y1 = p1
    x2, y2 = p2
    
    nx, ny = -(y2-y1), x2-x1

    xs, ys = x1 + (x2-x1)/3, y1 + (y2-y1)/3
    xu, yu = (x1+x2)/2 + nx*math.sqrt(3)/2/3 , (y1+y2)/2 + ny*math.sqrt(3)/2/3  
    xt, yt = x1 + (x2-x1)*2/3, y1 + (y2-y1)*2/3
    
    ps = xs, ys
    pu = xu, yu
    pt = xt, yt
    
    coh(n+1, p1, ps, pt_list, m)
    pt_list += [ps]
    coh(n+1, ps, pu, pt_list, m)
    pt_list += [pu]
    coh(n+1, pu, pt, pt_list, m)
    pt_list += [pt]
    coh(n+1, pt, p2, pt_list, m)

m = int(input())
pt_list = [(0,0)]
coh(1, (0,0), (100,0), pt_list, m)
pt_list += [(100,0)]
for xy in pt_list:
    print('%.9f %.9f'%(xy[0], xy[1]))
