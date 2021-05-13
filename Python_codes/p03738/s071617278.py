l = [int(input()) for i in range(2)]
a = 0
for n in l:
  if a == 0:
    a = n
  elif a > n:
    print('GREATER')
  elif a < n:
    print('LESS')
  else:
    print('EQUAL')