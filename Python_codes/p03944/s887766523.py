W,H,N=map(int,input().split())
W0,H0=0,0
for i in range(N):
    x,y,a=map(int,input().split())
    if a==1:
        W0=max(x,W0)
    elif a==2:
        W=min(x,W)
    elif a==3:
        H0=max(y,H0)
    else:
        H=min(y,H)
if W-W0<0 or H-H0<0:
    print(0)
else:
    print((W-W0)*(H-H0))