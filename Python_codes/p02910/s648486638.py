s = input()
n = len(s)
flg = True
for i in range(n):
  if i % 2 == 0 and s[i] == 'L':
    flg = False
    break
  elif i % 2 == 1 and s[i] == 'R':
    flg = False
    break

if flg:
  print('Yes')
else:
  print('No')