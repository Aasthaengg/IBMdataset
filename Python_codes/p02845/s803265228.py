n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
ans=1
cnt=[0]*(n+1)
cnt[0]=3
for i in range(n):
  if cnt[a[i]]>0:
    ans*=cnt[a[i]]%mod
    cnt[a[i]]-=1
    cnt[a[i]+1]+=1
  else:
    print(0)
    exit()
print(ans%mod)