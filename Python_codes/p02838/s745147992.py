n=int(input())
a=list(map(int,input().split()))
keta=[0]*61
for i in range(n):
  for j in range(61):
    if (a[i]>>j)&1==1:
      keta[j]+=1
ans=0
for i in range(61):
  ans+=((2**i)*(n-keta[i])*keta[i])%(10**9+7)
print(ans%(10**9+7))  
