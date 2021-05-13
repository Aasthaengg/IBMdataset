N = int(input())
moji = input()
r = 0
b = 0
for i in moji:
  if i == 'R':
    r += 1
  else:
    b += 1
if r > b:
  print('Yes')
else:
  print('No')