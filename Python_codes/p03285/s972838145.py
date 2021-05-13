n = int(input())
a = 25
b = 15

cnt = 0
for i in range(a + 1):
  for j in range(b + 1):
    if 4*i + 7*j == n:
      cnt += 1
if cnt >= 1:
  print('Yes')
else:
  print('No')