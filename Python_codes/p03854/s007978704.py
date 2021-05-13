import re

s = input()
flag = re.match('^(dream|dreamer|erase|eraser)+$',s)

if flag:
    print('YES')
else:
    print('NO')
