n, m, x, y = map(int, input().split())
xmax = max(list(map(int, input().split()))) + 1
ymin = min(list(map(int, input().split())))
if ymin - xmax < 0:
  print('War')
  exit()
for i in range(xmax, ymin + 1):
  if x < i <= y:
    print('No War')
    exit()
print('War')