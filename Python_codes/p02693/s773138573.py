k = int(input())
a, b = map(int,input().split())
if a % k == 0:
  print('OK')
elif a - a % k + k <= b:
  print('OK')
else:
  print('NG')