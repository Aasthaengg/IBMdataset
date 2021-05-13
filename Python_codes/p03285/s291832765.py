n = int(input())
count = 0
for i in range(16):
  if count:
    break
  if n - i * 7 == 0:
    print('Yes')
    count = 1
    break
  for j in range(26):
    if n - i * 7 - j * 4 == 0:
      print('Yes')
      count = 1
      break
if not(count):
  print('No')