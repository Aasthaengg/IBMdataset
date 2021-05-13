import itertools

n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=10**9+7
ans=0
a.sort()
a=list(itertools.accumulate(a))
pin=0


lst=[1,1]
for i in range(2,n+10):
  lst.append((lst[-1]*i)%mod)

def combinations(n,r):
  xxx=lst[n]
  xxx*=pow(lst[n-r],mod-2,mod)
  xxx%=mod
  xxx*=pow(lst[r],mod-2,mod)
  xxx%=mod

  return xxx

if k==1:
    print(0)
    exit()


for i in range(n-k+1):
  pin+=1
  now=n-k+1-i
  ans+=(a[-1]-a[-now-1]-a[now-1])*combinations(pin+k-3,k-2)
  ans%=mod


print(ans)