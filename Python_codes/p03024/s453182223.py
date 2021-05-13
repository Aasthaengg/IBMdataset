s = input()
k = len(s)
win = s.count('o')
if win + (15-k) >= 8:
  print('YES')
else:
  print('NO')