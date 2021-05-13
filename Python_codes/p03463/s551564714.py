n, a, b = list(map(int, input().split()))
if (b-a)%2 == 0:
  print('Alice')
elif (b-a)%2 == 1:
  print('Borys')
else:
  print('Draw')