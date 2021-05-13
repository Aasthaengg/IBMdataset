import re
a=input()
q=re.fullmatch(r'AtCoder(\s+)(\w+)(\s+)Contest',a)
print('A'+q.group(2)[0]+'C')
