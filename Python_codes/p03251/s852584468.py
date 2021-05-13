N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

xmax = max(x)
ymin = min(y)
if (xmax<ymin) and (xmax<Y) and (X<ymin):
  print('No War')
else:
  print('War')
