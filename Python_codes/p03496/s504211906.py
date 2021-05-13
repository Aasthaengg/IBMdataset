import numpy as np
n=int(input())
a=np.array(list(map(int,input().split())))

ma=np.max(a)
pma=np.argmax(a)
mi=np.min(a)
pmi=np.argmin(a)
ans=[]

if ma*mi<0:
    if abs(ma)>abs(mi):
        for i in range(n):
            if i==pma:
                continue

            ans.append((pma+1,i+1))
            a[i]+=ma
        pos=1
    else:
        for i in range(n):
            if i==pmi:
                continue

            ans.append((pmi+1,i+1))
            a[i]+=mi
        pos=0
else:
    if ma>0:
        pos=1
    else:
        pos=0

if pos==1:
    for i in range(1,n):
        if a[i]>=a[i-1]:
            continue
        ans.append((i,i+1))
        a[i]+=a[i-1]
else:
    for i in range(n-2,-1,-1):
        if a[i+1]>=a[i]:
            continue
        ans.append((i+2,i+1))
        a[i]+=a[i+1]

print(len(ans))

for x,y in ans:
    print('{} {}'.format(x,y))
