x = input().split()
n = int(x[0])
k = int(x[1])
if (n % k) == 0:
  print('0')
else:
  print('1')