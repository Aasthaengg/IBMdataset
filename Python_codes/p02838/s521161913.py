n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
ans=0

x=[0]*61

for i in range(61):
  for j in a:
    if (j>>i)%2==1:
      x[i]+=1


for i in a:
  for j in range(61):
    if (i>>j)%2==1:
      ans+=(n-x[j])*(2**j)


print(ans%mod)
