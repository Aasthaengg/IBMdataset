N = [str(e) for e in input().split()]
if(N[0] == 'H'):
  if(N[1] == 'H'):
    print('H')
  else:
    print('D')
else:
  if(N[1] == 'H'):
    print('D')
  else:
    print('H')