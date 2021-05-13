s = open(0).read().rstrip()

import re

if len(s)>3 and re.fullmatch(r'A[a-z]+C[a-z]+',s):
    print('AC')
elif len(s) == 3 and re.fullmatch(r'A[a-z]?C[a-z]?',s):
    print('AC')
else:
    print('WA')