import re
s = input()
ptn = re.compile(r'^A?KIHA?BA?RA?$')
result = ptn.match(s)
if result:
  print('YES')
else:
  print('NO')