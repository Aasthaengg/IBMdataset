s = input()
l = 0
for i in range(len(s)):
  if s[i] == 'x':
    l += 1
if l >= 8:
  print('NO')
else:
  print('YES')