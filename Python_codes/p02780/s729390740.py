import itertools

n,k=map(int,input().split())
a=list(map(int,input().split()))
a=list(map(lambda x:(x+1)/2,a))

a=[0]+list(itertools.accumulate(a))
ans=0

for i in range(n-k+1):
  ans=max(ans,a[i+k]-a[i])
  
print(ans)