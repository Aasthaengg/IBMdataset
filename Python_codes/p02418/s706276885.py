import re
s = input()
p = input()
s_loop = s + s
match = re.search(p, s_loop)
if not(match is None):
    print('Yes')
else:
    print('No')