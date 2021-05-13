s=list(map(int,input().split()))
a=sorted(s)
if a[0]<a[1]:
  if a[1]<a[2]:
    c=3
  else:
    c=2
else:
  if a[1]<a[2]:
    c=2
  else:
    c=1
print(c)