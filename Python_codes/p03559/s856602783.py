n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
ab=[]
bc=[]
for i in range(n):
    ab.append([a[i],n])
    bc.append([b[i],n])
    ab.append([b[i],i])
    bc.append([c[i],i])
numa=1
numb=1
numc=1
la=[1]*n
lb=[1]*n
lc=[1]*n
for i in range(1,n):
    if a[i-1]!=a[i]:
        la[i]=i+1
        numa=i+1
    else:
        la[i]=numa
    if b[i-1]!=b[i]:
        lb[i]=i+1
        numb=i+1
    else:
        lb[i]=numb
    if c[i-1]!=c[i]:
        lc[i]=i+1
        numc=i+1
    else:
        lc[i]=numc
ab.sort(key=lambda x: x[0])
numab=1
lab=[1]*(n+1)
for i in range(1,n*2):
    if ab[i-1][0]!=ab[i][0]:
        lab[ab[i][1]]=i+1
        numab=i+1
    else:
        lab[ab[i][1]]=numab
ansb=[0]*n
numb=0
for i in range(n):
    numb+=lab[i]-lb[i]
    ansb[i]=numb
bc.sort(key=lambda x: x[0])
numbc=1
lbc=[1]*(n+1)
for i in range(1,n*2):
    if bc[i-1][0]!=bc[i][0]:
        lbc[bc[i][1]]=i+1
        numbc=i+1
    else:
        lbc[bc[i][1]]=numbc
ansc=[0]*n
for i in range(n):
    ansc[i]=lbc[i]-lc[i]
ans=0
for i in range(n):
    if ansc[i]!=0:
        ans+=ansb[ansc[i]-1]
print(ans)
