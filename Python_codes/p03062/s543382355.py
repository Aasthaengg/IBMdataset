n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
  if i<0:
    c^=1

a=list(map(abs,a))
a.sort()
if c:
  print(sum(a)-a[0]*2)
else:
  print(sum(a))