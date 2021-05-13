N=int(input())
A=list(map(int,input().split()))
mod=10**9+7
ans=0
for i in range(60):
  X=1<<i
  n=len([1 for a in A if a&X])
  ans+=X*n*(N-n)%mod
  ans%=mod
print(ans)      
