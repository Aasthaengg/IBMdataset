s = input()
t = []
for c in s:
  t.append(c)
if sorted(t) == ['a', 'b', 'c']:
  print('Yes')
else:
  print('No')
