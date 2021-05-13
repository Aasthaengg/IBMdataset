s = input()
n = len(s)
t = 'keyence'
flg = False
for i in range(8):
  if i == 7:
    u = s[:7]
  else:
    u = s[:i] + s[i-7:]
  if u == t:
    flg = True
    break

if flg:
  print('YES')
else:
  print('NO')