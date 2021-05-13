N, Y = map(int, input().split())

for x in reversed(range(N + 1)): # 10000
  for y in reversed(range(N + 1 - x)): # 5000
    z = N - x - y
    if 10000*x  + 5000*y + 1000*z == Y:
      print(x, y, z)
      exit()
else:
	print(-1, -1, -1)