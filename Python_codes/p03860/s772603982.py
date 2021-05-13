import re
l = input()
l = l.split(' ')
s = l[1]
p = re.compile('^[A-Z][a-z]*')

result = ''
if 1 <= len(s) <= 100:
  if p.fullmatch(s):
    result = l[0][0] + s[0] + l[2][0]
print(result)