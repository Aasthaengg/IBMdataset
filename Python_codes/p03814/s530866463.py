import re
s = str(input())
a = re.search(r'A[A-Z]*Z', s)
print(len(a.group()))