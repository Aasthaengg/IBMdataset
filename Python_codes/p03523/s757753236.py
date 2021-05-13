import re
s = input()
if len(s) > 9: print('NO')
elif re.sub('A{,1}KIHA{,1}BA{,1}RA{,1}', '', s): print('NO')
else: print('YES')
