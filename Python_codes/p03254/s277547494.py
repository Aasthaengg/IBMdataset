n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for i in range(n):
  x-=a[i]
  if x < 0:
    n=i
    break
if x <=0:
  print(n)
elif x > 0:
  print(n-1)
