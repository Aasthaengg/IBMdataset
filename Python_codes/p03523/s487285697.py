import re

S = input()
L = 'A?KIHA?BA?RA?$'

if re.match(L, S):
    print('YES')
else:
    print('NO')