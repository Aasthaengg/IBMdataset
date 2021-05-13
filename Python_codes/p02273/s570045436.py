import math

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    

def kock(n,p1,p2):
    if n==0:
        return
    
    #calculate s,t,u from p1 and p2
    sx=(2*p1.x+1*p2.x)/3
    sy=(2*p1.y+1*p2.y)/3
    s=Point(sx,sy)
    tx=(1*p1.x+2*p2.x)/3
    ty=(1*p1.y+2*p2.y)/3
    t=Point(tx,ty)
    ux=(tx-sx)*math.cos(math.pi/3)-(ty-sy)*math.sin(math.pi/3)+sx
    uy=(tx-sx)*math.sin(math.pi/3)+(ty-sy)*math.cos(math.pi/3)+sy
    u=Point(ux,uy)

    kock(n-1,p1,s)
    print('{:.8f}'.format(s.x),'{:.8f}'.format(s.y))
    kock(n-1,s,u)
    print('{:.8f}'.format(u.x),'{:.8f}'.format(u.y))
    kock(n-1,u,t)
    print('{:.8f}'.format(t.x),'{:.8f}'.format(t.y))
    kock(n-1,t,p2)

p1=Point(0,0)
p2=Point(100,0)


n=int(input())
print('{:.8f}'.format(p1.x),'{:.8f}'.format(p1.y))
kock(n,p1,p2)
print('{:.8f}'.format(p2.x),'{:.8f}'.format(p2.y))
