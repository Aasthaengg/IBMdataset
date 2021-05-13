import re
s=input()
a=re.search('([0-9]{4})/([0-9]{2})/([0-9]{2})',s)
if int(a.group(2))>4:
    print('TBD')
else:
    print('Heisei')