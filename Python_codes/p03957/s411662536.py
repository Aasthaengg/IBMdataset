s = input()
idx = 0
flg = False
for i in range(len(s)):
  if s[i] == 'C':
    idx += 1
  elif s[i] == 'F' and idx > 0:
    flg = True
    break
if flg:
  print('Yes')
else:
  print('No')