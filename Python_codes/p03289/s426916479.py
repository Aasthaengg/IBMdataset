import sys
import re
S = input()
array_S = list(S)

if not ( 4 <= len(S) <= 10 ):
    print('WA')
    sys.exit()
if len(re.findall('[A-Z]',S)) != 2:
    print('WA')
    sys.exit()

result = 0
if array_S[0] != 'A': result += 1
if array_S[2:-1].count('C') != 1: result += 1 
array_S.pop(0)
array_S.pop(array_S.index('C'))
if not "".join(array_S).islower(): result += 1 
print('WA') if result != 0 else print('AC')