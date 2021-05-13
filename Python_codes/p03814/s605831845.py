import re
m = re.search('A[A-Z]*Z', input())
print(len(m.group()))