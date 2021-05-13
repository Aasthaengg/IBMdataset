from collections import defaultdict as dd
n=int(input())
s=input()
mod=10**9+7

d=dd(int)
for ss in s:
    d[ss]+=1

ans=1
for v in d.values():
    ans*=(v+1)
    ans%=mod
print((ans+mod-1)%mod)

