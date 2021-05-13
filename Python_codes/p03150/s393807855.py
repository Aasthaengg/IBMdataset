s = input()
k = 'keyence'

if k in s:
  print('YES')
  exit()
if s[0] == 'k' and s[-1] == 'e':
  for i in range(len(s)):
    if s.startswith(k[:i]) and s.endswith(k[i:]):
      print('YES')
      exit()
print('NO')