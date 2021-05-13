from itertools import zip_longest

o = input()
e = input()
s = ''
for i, j in zip_longest(o, e, fillvalue=''):
    s = s+i+j
print(s)