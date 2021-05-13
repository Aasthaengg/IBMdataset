a,b=[int(s) for s in input().split()]
if a*b*(a+b)%3==0:
  print('Possible')
else:
  print('Impossible')