import sys
class Pair:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class PPair:
    def __init__(self,xx,yy):
        self.xx=xx
        self.yy=yy

h,w=map(int,input().split())
A = [ list(map(int,input().split())) for i in range(h)]
odd =0
for i in range(h): 
    for j in range(w): 
        if A[i][j]%2==1: odd+=1
num=0;x=0;y=0
res=[]
for i in range(0,w*h):
    if A[x][y]%2==1: num+=1
    nx=x;ny=y;
    if x%2==0:
        if ny == w-1: nx+=1
        else: ny+=1
    else: 
        if ny==0: nx+=1
        else: ny-=1
    if num%2==1:
        if num<odd:
            res.append(PPair(Pair(x,y),Pair(nx,ny)))
    x=nx;y=ny
print (len(res))
for r in res:
    print("%d %d %d %d" %(r.xx.x+1, r.xx.y+1, r.yy.x+1, r.yy.y+1))
            
