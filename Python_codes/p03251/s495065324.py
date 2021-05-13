n, m, x, y = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

xx = max(xs)
yy = min(ys)

for i in range(x+1,y+1):
  if xx < i <= yy:
    print('No War')
    break
else:
  print('War')