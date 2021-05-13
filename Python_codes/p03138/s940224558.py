import sys

icase=0
if icase==0:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
elif icase==1:
    n,k=4,9
    a=[7,4,0,3]
elif icase==2:
    n,k=3,7
    a=[1,6,3]
elif icase==3:
    n,k=1,0
    a=[1000000000000]

if k==0:
    print(sum(a))
    sys.exit()
    
kk=[0]*42
kkk=k
kcnt=0
while kkk>0:
    kk[kcnt]=kkk%2
    kcnt+=1
    kkk=kkk//2
    
f=[0]*42
for ai in a:
    icnt=0
    while ai>0:
        f[icnt]+=ai%2
        ai=ai//2
        icnt+=1

n2=n//2+1
fm=[0]*42

flg1=0
flg2=0
for i in range(41,-1,-1):
    if flg1==0 and kk[i]==0:
        fm[i]=0
    if flg1==0 and kk[i]==1:
        flg1=1
    if flg1==0:
        fm[i]=f[i]        
        continue
#  case : flg1=1
    if kk[i]==1 and f[i]>=n2 and flg2==0:
        flg2=1
    if kk[i]==1 or (kk[i]==0 and flg2==1):
        if f[i]<n2:
            fm[i]=n-f[i]
        else:
            fm[i]=f[i]        
    else:
        fm[i]=f[i]        
    
smax=0
idx=1
for i in range(len(fm)):
    smax+=idx*fm[i]
    idx*=2

print(smax)
