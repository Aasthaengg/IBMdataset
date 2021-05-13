n,x = map(int,input().split())
a = sorted(list(map(int,input().split())))
c = 0
ans = 0
i = 0
while x>0 and i<n:
  x -= a[i]
  i += 1
  c += 1
  
if x==0:
  print(c)
else:
  print(c-1)