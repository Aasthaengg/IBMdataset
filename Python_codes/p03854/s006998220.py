S = input()

import re

if re.fullmatch(r'(dream|dreamer|erase|eraser)*', S):
    print('YES')
else:
    print('NO')