def check(a, b, c, word):
  if word == 'a':
    if not a:
      print('A')
      exit()
    check(a, b, c, a.pop(0))
  elif word == 'b':
    if not b:
      print('B')
      exit()
    check(a, b, c, b.pop(0))
  elif word == 'c':
    if not c:
      print('C')
      exit()
    check(a, b, c, c.pop(0))

a,b,c=list(input()),list(input()),list(input())
check(a, b, c, a.pop(0))