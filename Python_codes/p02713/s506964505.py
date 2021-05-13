k=int(input())
n=3
mod=10**9+7
lst=[0]*(k+1)
ans=0

for i in range(k,0,-1):
  lst[i]+=pow(k//i,n,mod)
  if k//i==1:
    continue
  else:
    for j in range(2,k//i+1):
      lst[i]-=lst[i*j]
      
for i in range(1,k+1):
  ans+=(i*lst[i])%mod
  ans%=mod
  
print(ans)