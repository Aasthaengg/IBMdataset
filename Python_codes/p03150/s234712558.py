from sys import stdin

s = stdin.readline().strip()
t_len = len(s) - 7

if t_len == 0:
  if s == 'keyence': print('YES')
  else: print('NO')
  exit()
else:
  for i in range(7):
    if s[:i] + s[i+t_len:] == 'keyence':
      print('YES')
      exit()
      
print('NO')