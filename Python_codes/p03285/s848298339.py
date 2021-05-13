N = int(input())
k = 0

for i in range(0, 26, 1):
  for j in range(0, 16, 1):
    if i * 4 + j * 7 == N:
      print('Yes')
      k = 1
      break
  if k == 1:
    break
else:
  if k != 1:
    print('No')