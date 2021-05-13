n = int(input())
now = [0, 0, 0]
def ng():
  print('No')
  exit()
for i in range(n):
  t, x, y = map(int, input().split())
  if t % 2 != (x + y) % 2:
    ng()
  if abs(x - now[1]) + abs(y - now[2]) > t - now[0]:
    ng()
  now = [t, x, y]
print('Yes')