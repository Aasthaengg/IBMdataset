s=input()
x,y=map(int,input().split())
lx=[]
ly=[]
t=0
k=0
for i in s:
    if i=="F":
        t+=1
    else:
        if k:
            ly.append(t)
            k=0
        else:
            lx.append(t)
            k=1
        t=0
if k:
    ly.append(t)
else:
    lx.append(t)
x-=lx.pop(0)
sx,sy=sum(lx),sum(ly)
dx=[0]*(sx*2+1)
dy=[0]*(sy*2+1)
dx[0],dy[0]=1,1
for i in lx:
    t=[0]*(sx*2+1)
    for j in range(-sx,sx+1):
        if dx[j]:
            t[i+j]=1
            t[j-i]=1
    dx=t
for i in ly:
    t=[0]*(sy*2+1)
    for j in range(-sy,sy+1):
        if dy[j]:
            t[i+j]=1
            t[j-i]=1
    dy=t
if sx>=abs(x) and sy>=abs(y) and dx[x] and dy[y]:
    print("Yes")
else:
    print("No")