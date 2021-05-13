n = input()
count = 0
for i in n:
  if i == '9':
    count = 1
if count == 1:
  print('Yes')
else:
  print('No')