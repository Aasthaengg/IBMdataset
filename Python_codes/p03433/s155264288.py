a = int(input())
b = int(input())


result = a % 500

if result - b <= 0:
  print('Yes')
else:
  print('No')