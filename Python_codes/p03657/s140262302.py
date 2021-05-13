a, b = map(int, input().split())
if (a + b) % 3 == 0:
  print('Possible')
  exit()
elif a % 3 == 0:
  print('Possible')
  exit()
elif b % 3 == 0:
  print('Possible')
  exit()
print('Impossible')