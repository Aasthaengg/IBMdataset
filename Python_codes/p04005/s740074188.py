a,b,c = [int(i) for i in input().split()]
if (a*b*c)%2==0:
  print(0)
else:
  print(min(a*b,a*c,b*c))