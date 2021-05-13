a = [int(input()) for i in range(2)]
n = a[0] % 500
if a[1] >= n:
  print('Yes')
else:
  print('No')