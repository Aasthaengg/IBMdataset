s = input()
l = len(s)
win = 0
for i in range(l):
  if s[i] == 'o':
    win += 1
if win + 15 - l >= 8:
  print('YES')
else:
  print('NO')
