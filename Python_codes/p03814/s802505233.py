import re
s = str(input())
a = re.findall('A[A-Z]*Z', s)
print(max(map(len, a)))