m, n = map(int, input().split())
total = m + n
if total % 2 == 0:
  print(total // 2)
else:
  print('IMPOSSIBLE')
