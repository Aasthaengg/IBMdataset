l=input()
mod=10**9+7
n=len(l)
ans=1
ans2=2
for i in range(1,n):
    ans=ans*3%mod
    if l[i]=="1":
        ans+=ans2
        ans2=ans2*2%mod
print((ans+ans2)%mod)