import re
 
S=input()
if len(S)>9:
  print('NO')
else:
  print('YES' if re.match('A?KIHA?BA?RA?',S) else 'NO')