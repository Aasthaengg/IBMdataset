n = int(input())
flag = False
for a in range(int(n / 7) + 1):
  for b in range(int(n / 4) + 1):
    if 7 * a + 4 * b == n:
      flag = True

if flag:
  print('Yes')
else:
  print('No')
