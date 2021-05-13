from re import match

p = 'A?KIHA?BA?RA?$'
s = input()

if (match(p, s)):
    print('YES')
else:
    print('NO')
