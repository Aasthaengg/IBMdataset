import re
S = input()
ans = re.fullmatch(pattern=r'A?KIHA?BA?RA?',string=S)
print('YES' if ans else 'NO')
