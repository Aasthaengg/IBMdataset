s=input()
num = 0
for x in s:
  if num == 0 and x == 'C':
    num += 1
  if num == 1 and x == 'F':
    num += 1
if num == 2:
  print('Yes')
else:
  print('No')