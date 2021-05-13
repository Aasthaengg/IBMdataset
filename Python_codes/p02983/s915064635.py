l,r=map(int,input().split())
mod=2019
ans=float("inf")
if l==0:
    print(0)
    exit()
for i in range(l,min(l+2021,r)):
    for j in range(i+1,min(r+1,l+2022)):
        tmp=(i*j)%mod
        if tmp<ans:
            ans=tmp
print(ans)