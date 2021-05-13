sa = input()
sb = input()
sc = input()
a = [sa[i] for i in range(len(sa))]
b = [sb[i] for i in range(len(sb))]
c = [sc[i] for i in range(len(sc))]

n = 'a'
while True:
  if n == 'a':
    if len(a) == 0:
      print('A')
      exit()
    else:
      n = a.pop(0)
  elif n == 'b':
    if len(b) == 0:
      print('B')
      exit()
    else:
      n = b.pop(0)
  elif n == 'c':
    if len(c) == 0:
      print('C')
      exit()
    else:
      n = c.pop(0)