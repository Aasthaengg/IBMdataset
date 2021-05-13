from itertools import zip_longest

o=input()
e=input()

print(''.join([x+y for x,y in zip_longest(o,e,fillvalue='')]))
