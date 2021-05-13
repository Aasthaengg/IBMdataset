a,b=map(str,input().split())

x={'H':1,'D':-1}

if x[a]*x[b]==1:
  print('H')
else:
  print('D')