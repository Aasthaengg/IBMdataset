x=[]

for j in range(100):
    m=j+1
    pf={}
    for i in range(2,int(m**0.5)+1):
        while m%i==0:
            pf[i]=pf.get(i,0)+1
            m//=i
    if m>1:pf[m]=1
    x.append(pf)

N=int(input())
if N==1:
    print(0)
    exit()

from collections import defaultdict
d=defaultdict(int)
for i in range(1,N):
    for k in x[i].keys():
        d[k]+=x[i][k]

#print(d)
over2=0
over4=0
over14=0
over24=0
over74=0
for k in d.keys():
    if d[k]>=2:
        over2+=1
    if d[k]>=4:
        over4+=1
    if d[k]>=14:
        over14+=1
    if d[k]>=24:
        over24+=1
    if d[k]>=74:
        over74+=1

ans=0
#case1
ans+=over4*(over4-1)//2*(over2-2)
#case2
ans+=over14*(over4-1)
#case3
ans+=over24*(over2-1)
#case4
ans+=over74
print(ans)