s = input()
win = 15 - len(s)
for i in range(len(s)):
  if s[i] == 'o':
    win += 1
print('YES' if win >= 8 else 'NO')