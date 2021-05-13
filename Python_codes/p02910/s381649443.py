s = input()
deff = 1
for i in range(len(s)):
  if (i % 2 == 0):
    if s[i] == 'L':
      deff = 0
  else:
    if s[i] == 'R':
      deff = 0
if deff == 1:
  print('Yes')
else:
  print('No')