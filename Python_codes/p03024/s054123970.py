s = str(input())
n = len(s)

w = 0
for i in range(n):
  if s[i] == 'o':
    w += 1
    
if w + (15 - n) >= 8:
  print('YES')
else:
  print('NO')