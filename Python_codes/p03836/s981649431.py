sx, sy, tx, ty=map(int,input().split())

dx=tx-sx
dy=ty-sy
d={0:'R', 1:'U', 2:'L', 3:'D'}
dirc=[dx,dy,dx,dy]

def path(sign,x,y,z,w):
  return d[sign+1]*abs(z-x) + d[sign+2]*abs(y-w)

s=''
s+='R'
s+=path(-1, sx+1, sy, tx, ty-1)
s+='UU'
s+=path(1, tx,ty+1,sx-1,sy)
s+='RD'
s+=path(-1, sx,sy-1,tx+1,ty)
s+='LL'
s+=path(1, tx-1,ty,sx,sy+1)
s+='D'
print(s)
