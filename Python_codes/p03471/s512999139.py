n, Y = map(int, input().split())

for x in range(n+1):
  for y in range(n+1):
    z = n - x - y
    if z >= 0 and 10000*x + 5000*y + 1000*z == Y:
      print("%d %d %d" % (x, y, z))
      exit()
print('-1 -1 -1')