n = int(input())
count = 0
for i in range(10):
  for j in range(10):
    if i*j == n:
      count = 1
      break

if count == 1:
  print('Yes')
else:
  print('No')