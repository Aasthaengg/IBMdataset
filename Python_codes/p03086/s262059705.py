import re
S = input()

strings = re.findall('[ACGT]*',S)

print(max(map(len,strings)))