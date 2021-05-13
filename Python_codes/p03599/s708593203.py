A,B,C,D,E,F=map(int,input().split())
A,B=A*100,B*100
water=[]
for i in range(F//A+1):
    for j in range(F//B+1):
        if A*i+B*j<=F and not(i==0 and j==0):
            water.append((A*i+B*j))
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