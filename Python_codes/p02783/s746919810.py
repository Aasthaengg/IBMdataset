hp, attack = map(int, input().split())

x, y = divmod(hp, attack)

if y == 0:
	print(x)
else:
  	print(x + 1)
