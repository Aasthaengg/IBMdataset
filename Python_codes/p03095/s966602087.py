mod=10**9+7

N=int(input())
S=input()

d={}
for s in S:
    if s in d:
        d[s]+=1
    else:
        d[s]=1
ans=1
for D in d:
    ans*=d[D]+1
    ans%=mod
print((ans-1)%mod)