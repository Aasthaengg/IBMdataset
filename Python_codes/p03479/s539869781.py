x, y = map(int, input().split())
res = 1
for i in range(100):
  x *= 2
  if x <= y:
    res += 1
  else:
    print(res)
    exit()