n,t= map(int,input().split())
a= list(map(int,input().split()))
mp,mprof = 999999999,0
bid = []
bsus = []
sid = []
nc=0
for i in range(n):
    cp = a[i]-mp
    if cp<0:
        nc += min(len(bid),len(sid))
        mp = a[i]
        sid=[]
        bid=[]
        bsus=[i]
    elif cp>0:
        if mprof <= cp:
            bid += bsus
            bsus = []
            if mprof < cp:
                mprof,sid,nc = cp,[i],0
            else:sid.append(i)
    else:bsus.append(i)
else:
    if len(bid)!=0 and len(sid)!=0:
        nc += min(len(bid),len(sid))
print(nc)