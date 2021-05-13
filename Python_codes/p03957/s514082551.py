import re
s = input()
m = re.compile('[A-Z]*C[A-Z]*F[A-Z]*')
if m.fullmatch(s):
  print('Yes')
else:
  print('No')