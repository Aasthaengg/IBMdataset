mod = 10 ** 9 + 7
x = 1
y = 0
for c in input():
	if c == "1":
		y *= 3
		y %= mod
		y += x
		y %= mod
		x *= 2
		x %= mod
	else:
		y *= 3
		y %= mod
print((x + y) % mod)