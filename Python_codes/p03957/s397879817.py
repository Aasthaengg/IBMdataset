import re
s = input()
s = re.sub('[^F^C]', '', s)
if s.count('CF') > 0: print('Yes')
else: print('No')
