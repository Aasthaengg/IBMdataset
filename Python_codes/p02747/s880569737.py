import re
text = input()
if re.fullmatch('(hi)+', text) != None:
    print('Yes')
else:
    print('No')