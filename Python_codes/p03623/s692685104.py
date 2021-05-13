x,a,b=[int(i) for i in input().split()]
n=abs(a-x)
m=abs(b-x)
if n>m:
  print('B')
else:
  print('A')