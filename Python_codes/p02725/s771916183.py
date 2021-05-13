k,n=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for x in range(n-1):
  b=a[x+1]-a[x]
  ans=max(ans,b)
  
c=k-a[n-1]+a[0]

print(k-max(ans,c))

