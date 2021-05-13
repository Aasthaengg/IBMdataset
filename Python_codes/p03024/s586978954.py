s = input()
o = 15 - len(s)
for i in range(len(s)):
  if s[i] == 'o': o += 1
if (o >= 8): print('YES')
else: print('NO')