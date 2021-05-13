import re
s = input()
a = re.search(r'\d{4}/(\d)(\d)/\d{2}', s)
if a.group(1) == '0' and (a.group(2) == '1' or a.group(2) == '2' or a.group(2) == '3' or a.group(2) == '4'):
    print('Heisei')
else:
    print('TBD')