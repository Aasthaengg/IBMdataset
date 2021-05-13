x, y = map(int, input().split())

if x == y:
  print(-1)
  exit()

if y == 1:
  print(-1)
  exit()

for i in range(1, y):
  temp = x * i
  if temp <= 10 ** 18 and temp % y != 0:
    print(x*i)
    exit()

print(-1)