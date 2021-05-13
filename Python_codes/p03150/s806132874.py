import re

S = input()

if S == 'keyence' or re.fullmatch(r'[a-z]+keyence', S) or re.fullmatch(r'k[a-z]+eyence', S) or re.fullmatch(r'ke[a-z]+yence', S) or re.fullmatch(r'key[a-z]+ence', S) or re.fullmatch(r'keye[a-z]+nce', S) or re.fullmatch(r'keyen[a-z]+ce', S) or re.fullmatch(r'keyenc[a-z]+e', S) or re.fullmatch(r'keyence[a-z]+', S):
  print('YES')
else:
  print('NO')