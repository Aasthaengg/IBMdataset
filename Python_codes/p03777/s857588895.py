def another(s):
  if s == 'D':
    return 'H'
  else:
    return 'D'

a, b = input().split()
if a == 'H':
  print(b)
else:
  print(another(b))
