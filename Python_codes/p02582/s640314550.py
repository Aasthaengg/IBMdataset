import re

x = input()
pattern = "R+"
pat = re.search(pattern, x)
if pat:
  print(len(pat.group()))
else:
  print(0)