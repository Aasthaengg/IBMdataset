N,K=map(int,input().split())
point=[list(map(int,input().split())) for _ in range(N)]
ans=10**30
#print(ans)
#print(Decimal(1999999999)*Decimal(1999999999))
#print(1999999999*1999999999)
for i in range(N):
    for j in range(i,N):
        x1,_=point[i]
        x2,_=point[j]
        minx=min(x1,x2)
        maxx=max(x1,x2)
        for k in range(N):
            for l in range(k,N):
                _,y1= point[k]
                _,y2= point[l]
                miny = min(y1,y2)
                maxy = max(y1,y2)
                cnt=0
                menseki=(maxx-minx)*(maxy-miny)
                for m in range(N):
                    x,y=point[m]
                    if (minx<=x<=maxx)and(miny<=y<=maxy):
                        cnt=cnt+1
                if cnt>=K:
                    ans=min(ans,menseki)
print(ans)

"""
for i in range(N):
    for j in range(i+1,N):
        #print(i,j)
        menseki=Decimal(1)
        x1,y1=point[i]
        x2,y2=point[j]
        if x1<x2:
            abx=Decimal(x2)-Decimal(x1)
        else:
            abx=Decimal(x1)-Decimal(x2)
        if y1<y2:
            aby=Decimal(y2)-Decimal(y1)
        else:
            aby=Decimal(y1)-Decimal(y2)
        print("")
        print(abx,aby)
        menseki=abx*aby
        print(menseki)
        minx=min(x1,x2)
        maxx=max(x1,x2)
        miny=min(y1,y2)
        maxy=max(y1,y2)
        pnum=0
        print(minx,maxx,miny,maxy)
        for x,y in point:
            #print(x,y)
            if (minx<=x<=maxx)and(miny<=y<=maxy):
                pnum=pnum+1
        print(pnum)
        if pnum>=K:
            ans=ans.min(menseki)
            print(ans)
print(ans)
"""