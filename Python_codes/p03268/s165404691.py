n,k=map(int,input().split())
mods=[0]*k
mods[0]=n//k
for i in range(1,k):
    mods[i]=(n-i)//k+1
ans=0

for i in range(k):
    if (2*k-i)%k == i:
        ans+=mods[i]**3
print(ans)