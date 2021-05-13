import re

s = input()
p = re.compile('C.*F')
m = re.search(p, s)
print('Yes' if m is not None else 'No')
