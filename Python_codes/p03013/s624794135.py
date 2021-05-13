N,M=map(int,input().split())
ans=[0 for i in range(N+1)]
true=[True for i in range(N+1)]
for i in range(M):
  a=int(input())
  true[a]=False
mod=10**9+7
ans[0]=1
ans[1]=1
for i in range(2,N+1):
  for j in range(i-2,i):
    if true[j]:
      ans[i]+=ans[j]%mod
print(ans[N]%mod)