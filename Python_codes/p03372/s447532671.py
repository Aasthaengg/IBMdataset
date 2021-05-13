n,c=map(int,input().split())


kyori=[0]*(n+2)
kyori[n+1]=c
calo=[0]*(n+2)
ans=[0]
tmp=0

for i in range(1,n+1):
    x,v=map(int,input().split())
    kyori[i]=x
    calo[i]=v
    tmp+=v-(x-kyori[i-1])
    ans.append(tmp)


tmp=0
for i in range(n):
    tmp+=calo[-2-i] - (kyori[-1-i]-kyori[-2-i])
    ans.append(tmp)


i=1
rmax=0
tmpmax=0
tmp=0
while(2*kyori[i]< c and i<=n):
    tmp+=calo[i]-2*(kyori[i] -kyori[i-1])
    if(tmpmax<tmp):
        tmpmax=tmp
        rmax=i
    i+=1


tmp=0
tmpmax_max=0
i=0
while(rmax < -i+n):
    tmp+=calo[-2-i] - (kyori[-1-i] - kyori[-2-i])
    if(tmpmax_max<tmp):
        tmpmax_max=tmp
    i+=1
ans.append(tmpmax+ tmpmax_max)


now=tmpmax+ tmp
for i in range(rmax):
    tmpmax+= -calo[rmax-i]+2*(kyori[rmax-i] - kyori[rmax-i-1])
    tmp+=calo[rmax-i] -(kyori[rmax+1-i]-kyori[rmax-i])
    if(tmpmax_max<tmp):
        tmpmax_max=tmp
    ans.append(tmpmax+tmpmax_max)




i=0
lmax=0
tmpmax=0
tmp=0
while(2*kyori[-2-i] > c and i<n):
    tmp+=calo[-2-i]-2*(kyori[-1-i] -kyori[-2-i])
    if(tmpmax<tmp):
        tmpmax=tmp
        lmax=-i+n
    i+=1
if(lmax==0):
    lmax=n+1
tmp=0
tmpmax_max=0
i=1
while(i < lmax):
    tmp+=calo[i] - (kyori[i] - kyori[i-1])
    if(tmpmax_max <tmp):
        tmpmax_max=tmp
    i+=1

ans.append(tmpmax+ tmpmax_max)



now=tmpmax+ tmp
for i in range(n-lmax):
    tmpmax+= -calo[lmax+i]+2*(kyori[lmax+i+1] - kyori[lmax+i])
    tmp+=calo[lmax+i] -(kyori[lmax+i]-kyori[lmax+i-1])
    if(tmpmax_max<tmp):
        tmpmax_max=tmp
    ans.append(tmpmax+tmpmax_max)





print(max(ans))