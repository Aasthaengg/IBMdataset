from collections import Counter
S = tuple(input())
c = Counter(S)
if not c['a']:
  c['a'] = 0
if not c['b']:
  c['b'] = 0
if not c['c']:
  c['c'] = 0
if max(c.values()) - min(c.values()) < 2:
  print('YES')
else:
  print('NO')