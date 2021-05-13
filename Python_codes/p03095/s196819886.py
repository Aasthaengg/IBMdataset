n=int(input())
s=input()
d=dict(zip([chr(97+i) for i in range(26)],[1]*26))
mod=10**9+7
for i in s:
  d[i]+=1
ans=1
for i in d.values():
  ans*=i
  ans%=mod
print((ans-1)%mod)