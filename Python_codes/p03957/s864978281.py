import re
s = input()
reg = '[A-Z]*C[A-Z]*F[A-Z]*'
res = re.fullmatch(reg, s)
if res:
    print('Yes')
else:
    print('No')