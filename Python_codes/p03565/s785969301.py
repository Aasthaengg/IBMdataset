import re

_S = input().replace('?', '_')[::-1]
T = input()[::-1]

pattern = ''
for c in T:
    pattern += '[_' + c + ']'

match = re.search(pattern, _S)
if not match:
    print('UNRESTORABLE')
else:
    S = _S[:match.start()] + T + _S[match.end():]
    S = S.replace('_', 'a')
    print(S[::-1])
