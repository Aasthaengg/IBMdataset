n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for i in range(n):
  if a[i]>x:
    print(i)
    exit()
  x-=a[i]
if x==0:
  print(n)
else:
  print(n-1)
