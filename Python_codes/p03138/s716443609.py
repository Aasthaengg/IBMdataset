n,k=map(int,input().split())
l=list(map(int,input().split()))
keta=[0 for i in range(41)]
for i in l:
    for j in range(41):
        keta[j]+=i%2
        i//=2
ans=0
t=0
x=40
k2=[0 for i in range(41)]
for j in range(41):
    k2[j]=k%2
    k//=2
for i in k2[::-1]:
    if i==0 and t==0:
        ans+=keta[x]*(2**x)
    else:
        if keta[x]>n//2:
            if i==1:
                t=1
            ans+=keta[x]*(2**x)
        else:
            ans+=(n-keta[x])*(2**x)
    x-=1
print(ans)