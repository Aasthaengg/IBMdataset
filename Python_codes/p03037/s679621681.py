n,m=map(int,input().split())
L=[]
R=[]
for i in range(m):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)
LL=max(L)
RR=min(R)
if LL<=RR:
    print(RR-LL+1)
else:
    print(0)