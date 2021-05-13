import re

s = input()

if re.match(r'A[a-z]+C[a-z]+$', s):
    print('AC')
else:
    print('WA')