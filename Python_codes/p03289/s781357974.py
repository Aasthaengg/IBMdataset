import re
S = input()
if re.match(r'^A[a-z][a-z]*?C[a-z]*?[a-z]$', S):
    print('AC')
else:
    print('WA')
