
sx,sy,tx,ty=map(int,input().split())
dx=tx-sx
dy=ty-sy
s=''
route=['U' for i in range(dy)]
for i in range(dx):
    route.append('R')
for i in range(dy):
    route.append('D')
for i in range(dx+1):
    route.append('L')
for i in range(dy+1):
    route.append('U')
for i in range(dx+1):
    route.append('R')
route.append('D')
route.append('R')
for i in range(dy+1):
    route.append('D')
for i in range(dx+1):
    route.append('L')
route.append('U')
for i in range(len(route)):
    s+=route[i]
print(s)
