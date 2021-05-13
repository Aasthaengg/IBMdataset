a,b=[int(i) for i in input().split()]
if a==b:
  print(2*a)
else:
  print(max(a,b)+(max(a,b)-1))