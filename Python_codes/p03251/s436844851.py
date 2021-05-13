N, M, X, Y = map(int, input().split())
x = max(list(map(int, input().split())))
y = min(list(map(int, input().split())))
if y - x > 0:
  if X < x < Y or X < y <= Y:
  	print('No War')
  else:
    print('War')
else:
  print('War')