import re
n = input()

if re.search(r'(\d)\1{2,}', n):
    print('Yes')
else:
    print('No')