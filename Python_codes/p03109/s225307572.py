import re
s=input()
a=re.search('([0-9]{4})/([0-9]{2})/([0-9]{2})',s)
if int(str(a.group(2)))<=4:
    print('Heisei')
else:
    print('TBD')