O = input()
E = input()
if len(O) > len(E):
  print(''.join([o+e for o, e in zip(O,E)] + [O[-1]]))
else:
  print(''.join([o+e for o, e in zip(O,E)]))