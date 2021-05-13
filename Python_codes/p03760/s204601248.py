O = input()
E = input() + ' '
print(''.join([o+e.strip() for o,e in zip(O,E)]))