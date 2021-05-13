import re
s=input()
S=re.sub(r'([0-9]{4})/([0-9]{2})/([0-9]{2})',r'\1\2\3',s)
if int(S)<=20190430:
    print('Heisei')
else:
    print('TBD')