import re
print('NYOE S'[bool(re.match('^(dream|dreamer|erase|eraser)+$',input()))::2])