n,x=map(int,input().split())
a=[0]+list(map(int,input().split()))

cnt=0
for i in range(n):
  t=max(a[i]+a[i+1]-x,0)
  cnt+=t
  a[i+1]-=t
print(cnt)