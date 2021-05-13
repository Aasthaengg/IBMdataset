n,k=map(int,input().split())
mods=[0]*k
mods[0]=n//k
for i in range(1,k):
    mods[i]=(n-i)//k+1
# print(mods)
ans=0

for i in range(k):
    if (k-i)%k == i:
        ans+=mods[i]*mods[(k-i)%k]*mods[i]
print(ans)