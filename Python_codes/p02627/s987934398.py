import re
a = input()
mo = re.search(r'[a-z]', a)
if mo is None:
    print('A')
else:
    print('a')