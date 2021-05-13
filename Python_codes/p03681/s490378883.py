N,M=map(int,input().split())
ans=1
mod=10**9+7
if N>M+1 or M>N+1:
  print(0)
  exit()
for i in range(1,N+1):
  ans*=i
  ans%=mod
for j in range(1,M+1):
  ans*=j
  ans%=mod
if N==M:
  ans=ans*2%mod
print(ans)