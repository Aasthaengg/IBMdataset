n=int(input())
a=list(map(int,input().split()))
a+=a
for i in range(2*n):
  if i%2:a[i]=-a[i]
for i in range(2*n-1):
  a[i+1]+=a[i]
a=[0]+a
for i in range(n):
  print(abs(a[n+i]-a[i]))