from collections import Counter
input()
cnt=Counter(input())

ans=1
mod=10**9+7

for v in cnt.values():
    ans*=v+1
    ans%=mod

print((ans-1)%mod)