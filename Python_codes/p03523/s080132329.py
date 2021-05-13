import re

S = input()
pat = r'A?KIHA?BA?RA?$'
print('YES' if re.match(pat, S) else 'NO')