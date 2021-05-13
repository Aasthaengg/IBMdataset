import re
pattern = re.compile('[ACGT]+')
S = input()
print(len(max(re.findall(pattern, S), key=len, default='')))