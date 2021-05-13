import re
s = input()
reg = "A?KIHA?BA?RA?"
res = re.fullmatch(reg, s)
if res:
    print('YES')
else:
    print('NO')
