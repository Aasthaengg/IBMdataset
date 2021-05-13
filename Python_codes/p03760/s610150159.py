from itertools import zip_longest
o = input()
e = input()
for i, j in zip_longest(o,e,fillvalue=''):
  print(i+j, end='')