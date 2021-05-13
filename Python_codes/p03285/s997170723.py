N = int(input())

a = N // 7

for i in range(a+1):
  b = N - i * 7
  if b%4 == 0:
    print('Yes')
    break
  else:
    continue
else:
  print('No')
