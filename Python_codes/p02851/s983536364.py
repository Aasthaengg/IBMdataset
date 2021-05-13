n,k=map(int,input().split())
l=list(map(int,input().split()))
if k==1:
    print(0)
    exit()
nl=[]
for i in range(n):
    nl.append((l[i]-1)%k)
r=[0]*(n+1)
for i in range(n):
    r[i+1]=(r[i]+nl[i])%k
p=[]
for i in range(n+1):
    p.append([r[i],i])
p.sort()
s=0
e=0
ans=0
f=0
while e<n+1:
    if p[s][0]!=p[e][0]:
        ans+=f*(f-1)//2
        s=e
        f=0
    else:
        if p[s][1]+k-1>=p[e][1]:
            f+=1
            e+=1
        else:
            ans+=f-1
            f-=1
            s+=1
print(ans+f*(f-1)//2)
