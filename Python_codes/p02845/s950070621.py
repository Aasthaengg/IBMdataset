n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  a[i]+=1
cnt=[0]*(n+1)
cnt[0]=3
ans=1
mod=10**9+7
for i in range(n):
  if cnt[a[i]-1]>0:
    ans*=cnt[a[i]-1]%mod
    cnt[a[i]-1]-=1
    cnt[a[i]]+=1
  else:
    print(0)
    exit()
print(ans%mod)