n=int(input())
a=[False]*(n+10)
a[0]=True
for i in range(n+1):
  if a[i]:
    a[i+4]=True
    a[i+7]=True
if a[n]:
  print("Yes")
else:
  print("No")