import re
s = input()
num = len(s)
s = re.sub('A[A-Z]*Z', '', s)
print(num-len(s))
