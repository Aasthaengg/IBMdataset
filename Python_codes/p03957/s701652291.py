s = input()
n = len(s)
cnt = 0
for i in range(n):
  if cnt == 0 and s[i] == 'C':
    cnt += 1
  elif cnt == 1 and s[i] == 'F':
    cnt += 1
    break
if cnt >= 2:
  print('Yes')
else:
  print('No')