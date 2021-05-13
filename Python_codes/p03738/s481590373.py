al = list(map(int, input()))
bl = list(map(int, input()))
if len(al) > len(bl):
  print('GREATER')
  quit()
elif len(al) < len(bl):
  print('LESS')
  quit()
for a, b in zip(al, bl):
  if a > b:
    print('GREATER')
    quit()
  elif a < b:
    print('LESS')
    quit()
else:
  print('EQUAL')