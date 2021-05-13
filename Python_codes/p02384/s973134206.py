c=[int(i) for i in input().split()]
Q=int(input())
inp=[map(int,input().split()) for i in range(Q)]
d=[(0,0,1),(-1,0,0),(0,1,0),(0,-1,0),(1,0,0),(0,0,-1)]
def north(r):
    res=[]
    for p in r:
        res.append((p[2],p[1],-p[0]))
    return res
def south(r):
    res=[]
    for p in r:
        res.append((-p[2],p[1],p[0]))
    return res
def east(r):
    res=[]
    for p in r:
        res.append((p[0],p[2],-p[1]))
    return res
def west(r):
    res=[]
    for p in r:
        res.append((p[0],-p[2],p[1]))
    return res
for k in range(Q):
    x=(0,0,0)
    y=(0,0,0)
    a,b=inp[k]
    for i in range(6):
        if a==c[i]:
            x=d[i]
        if b==c[i]:
            y=d[i]
    z=(y[1]*x[2]-y[2]*x[1],y[2]*x[0]-y[0]*x[2],y[0]*x[1]-y[1]*x[0])
    for i in range(6):
        if d[i]==z:
            print(c[i])
