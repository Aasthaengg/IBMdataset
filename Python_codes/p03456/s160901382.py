a = input()
b = int(a.replace(' ', ''))

c = b**(1/2)

if c.is_integer():
  print('Yes')
else:
  print('No')