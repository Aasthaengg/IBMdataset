k,n=map(int,input().split())
a=list(map(int,input().split()))
m=-10000
for i in range(1,n):
  x=a[i]-a[i-1]
  m=max(m,x)

print(min((k-m),abs(a[n-1]-a[0])))