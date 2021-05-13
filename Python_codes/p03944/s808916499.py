W,H,N=map(int,input().split())
W0=0
H0=0
for i in range(N):
    x1,y1,a1=map(int,input().split())
    if a1 ==1 and W0<x1:
        W0=x1
    elif a1==2 and W>x1:
        W=x1
    elif a1==3 and H0<y1:
        H0=y1
    elif a1==4 and H>y1:
        H=y1

if W-W0>0 and H-H0>0:
    print((W-W0)*(H-H0))
else:
    print(0)