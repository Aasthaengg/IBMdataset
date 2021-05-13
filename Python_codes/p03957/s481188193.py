import re
s = input()
if re.search(r'.*C.*F.*', s) != None:
    print('Yes')
else:
    print('No')