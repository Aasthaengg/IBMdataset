N,K=map(int,input().split())
mod=10**9+7
c=[1]
for i in range(1,N+1):
  c+=[c[i-1]*i]

def cmb(a,b):
  return c[a]//c[a-b]//c[b]
  
for i in range(1,K+1):
  if N-K<i-1 or K<i:
    print(0);continue
  
  m=cmb(K-1,i-1)%mod
  n=cmb(N-K+1,i)%mod
  ans=m*n%mod
  print(ans)