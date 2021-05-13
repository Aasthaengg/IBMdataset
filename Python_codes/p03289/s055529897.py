import re
s = input()
p = re.compile('[a-z]+')
ans = ''
if s[0] == 'A' and s[2:-1].count('C') == 1:
  s = s.replace('A', '').replace('C', '')
  if p.fullmatch(s):
    ans = 'AC'
  else:
    ans = 'WA'
else:
  ans = 'WA'
print(ans)