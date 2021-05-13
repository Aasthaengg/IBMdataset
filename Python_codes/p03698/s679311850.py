s = input()
l = len(s)
m = set()
for i in range(l):
  m.add(s[i])
m = len(list(m))
if l == m:
  print('yes')
else:
  print('no')