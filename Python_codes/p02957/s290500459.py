a,b = map(int,input().split())

sa = max(a,b) - min(a,b)

if sa % 2 == 0:
  print((a + b) // 2)
else:
  print('IMPOSSIBLE')