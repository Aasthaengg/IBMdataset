A,B,C,D,E,F=map(int,input().split())
wDP=[False]*((F//100)+1)
wDP[0]=True
water=[]
for i in range(1,(F//100)+1):
    if(i>=B and wDP[i-B]):
        wDP[i]=True
    elif(i>=A and wDP[i-A]):
        wDP[i]=True
for i in range((F//100)+1):
    if(wDP[i] and i!=0):
        water.append(i*100)
water=list(set(water))
ans=[water[0],0]
mconc=0
for x in water:
    up=min(x*E//100,F-x)
    sDP=[0]*(up+1)
    for i in range(1,up+1):
        if(i>=D):
            sDP[i]=max(sDP[i-1],sDP[i-C]+C,sDP[i-D]+D)
        elif(i>=C):
            sDP[i]=max(sDP[i-1],sDP[i-C]+C)
        else:
            sDP[i]=sDP[i-1]
    conc=100*sDP[-1]/(x+sDP[-1])
    if(conc>=mconc):
        mconc=conc;ans[0]=x+sDP[-1];ans[1]=sDP[-1]
print(*ans)