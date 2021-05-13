import re
S = input()
print(len(max(re.findall('[ACTG]+', S), key=len, default='')))