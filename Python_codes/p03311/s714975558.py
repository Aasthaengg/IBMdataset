n=int(input())
a=list(map(int,input().split()))
b=[0]*n
for i in range(n):
  b[i]=a[i]-(i+1)
b.sort()
if n%2==1:
  ans=b[(n-1)//2]
  an=0
  for i in range(n):
    an+=abs(a[i]-ans-i-1)
  print(an)
else:
  ans=(b[n//2]+b[n//2-1])//2
  an=0
  for i in range(n):
    an+=abs(a[i]-ans-i-1)
  print(an)
