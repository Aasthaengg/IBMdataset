s = input()
rest = 15 - len(s)
t = 'o'
t = t*rest
posibble = s + t
if posibble.count('o') >= 8:
  print('YES')
else:
  print('NO')
