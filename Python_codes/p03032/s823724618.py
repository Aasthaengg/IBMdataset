import sys

n,k0=map(int,input().split())
v=list(map(int,input().split()))

k=k0
if n<=k:
    v.sort()
    vsum=sum(v)
    kk=k-n
    vsum=0
    for i in range(n):
        if i>kk:
            vsum+=v[i]
        elif i<=kk and v[i]>0:
            vsum+=v[i]
    print(max(0,vsum))
    sys.exit()

vmax=-10**10

kk=k0
for k in range(kk):
    k2=kk-k-1
    
    vv=[[0]*(k+1) for i in range(k+1+1)]
    for i in range(k+1):
        vv[0][i]=v[n-k+i-1]
    vsum=sum(vv[0])
    vmax=max(vsum,vmax)
#    print("k:",k,"vsum:",vsum,"vmax:",vmax)
#    print(vv[0])
    vvv=vv[0].copy()
    vvv.sort()
    for i in range(min(k2,k+1)):
        if vvv[i]<0:
            vsum-=vvv[i]
    vmax=max(vsum,vmax)
#    print("k:",k,"vsum:",vsum,"vmax:",vmax)

    for i in range(k+1):
        vv[i+1]=vv[i].copy()
        vv[i+1].pop(0)
        vv[i+1].append(v[i])
        vsum=sum(vv[i+1])
        vmax=max(vsum,vmax)
#        print("k:",k,"vsum:",vsum,"vmax:",vmax)
#        print(vv[i+1])
        vvv=vv[i+1].copy()
        vvv.sort()
        for i in range(min(k2,k+1)):
            if vvv[i]<0:
                vsum-=vvv[i]
        vmax=max(vsum,vmax)
#        print("k:",k,"vsum:",vsum,"vmax:",vmax)
    
print(max(0,vmax))    

