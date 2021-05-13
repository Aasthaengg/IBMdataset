n,x=map(int, input().split())
a=[0]+list(map(int, input().split()))
ans=0
for i in range(n):
  eat=max(a[i]+a[i+1]-x,a[i+1]-2*x,0)
  ans+=eat
  a[i+1]-=eat
print(ans)