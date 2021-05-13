a=list(map(int,input().split()))
a.sort()
if a[0]==a[1]==a[2]:
  print(1)
else:
  if a[0]==a[1] or a[1]==a[2] or a[2]==a[0]:
    print(2)
  else:
    print(3)