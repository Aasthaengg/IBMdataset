n = input().split()
a = n[0]
b = n[1]
if a == 'H':
  if b == 'H':
    print('H')
  else:
   print('D') 
else:
  if b == 'H':
    print('D')
  else:
    print('H')
